import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedTool, setSelectedTool] = useState(null);
  const [drawingShape, setDrawingShape] = useState(null);
  const [shapes, setShapes] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [numRows, setNumRows] = useState(1);
  const [numColumns, setNumColumns] = useState(1);
  const [selectedShapes, setSelectedShapes] = useState([]); // State to track selected shapes

  const handleCanvasClick = (event) => {
    if (selectedTool === 'rectangle' && !drawingShape) {
      const newDrawingShape = {
        type: 'rectangle',
        startX: event.clientX,
        startY: event.clientY,
        endX: event.clientX,
        endY: event.clientY,
      };
      setDrawingShape(newDrawingShape);
    } else if (selectedTool === 'rectangle' && drawingShape) {
      const newRectangle = {
        type: 'rectangle',
        left: Math.min(drawingShape.startX, drawingShape.endX),
        top: Math.min(drawingShape.startY, drawingShape.endY),
        width: Math.abs(drawingShape.endX - drawingShape.startX),
        height: Math.abs(drawingShape.endY - drawingShape.startY),
      };
      setShapes([...shapes, newRectangle]);
      setDrawingShape(null);
      setSelectedTool(null); // Draw Rectangle 버튼 비활성화
    } else if (selectedTool === 'table') {
      // Open modal for setting table dimensions
      setModalOpen(true);
    }
  };

  const handleMouseMove = (event) => {
    if (drawingShape) {
      setDrawingShape(prevDrawingShape => ({
        ...prevDrawingShape,
        endX: event.clientX,
        endY: event.clientY,
      }));
    }
  };

  const handleToolSelect = (tool) => {
    setSelectedTool(tool);
  };

  const handleShapeDrag = (event, index) => {
    const { left, top } = shapes[index];
    const offsetX = event.clientX - left;
    const offsetY = event.clientY - top;

    const handleDragMove = (event) => {
      const newLeft = event.clientX - offsetX;
      const newTop = event.clientY - offsetY;

      setShapes(prevShapes => {
        const updatedShapes = [...prevShapes];
        updatedShapes[index] = {
          ...updatedShapes[index],
          left: newLeft,
          top: newTop,
        };
        return updatedShapes;
      });
    };

    const handleDragEnd = () => {
      document.removeEventListener('mousemove', handleDragMove);
      document.removeEventListener('mouseup', handleDragEnd);
    };

    document.addEventListener('mousemove', handleDragMove);
    document.addEventListener('mouseup', handleDragEnd);
  };

  const handleModalClose = () => {
    setModalOpen(false);
  };

  const handleTableCreate = () => {
    // Create table based on numRows and numColumns
    for (let i = 0; i < numRows; i++) {
      for (let j = 0; j < numColumns; j++) {
        const newRectangle = {
          type: 'rectangle',
          left: 100 + j * 100, // Adjust position based on grid size
          top: 100 + i * 100, // Adjust position based on grid size
          width: 90, // Adjust size based on grid size
          height: 90, // Adjust size based on grid size
        };
        setShapes(prevShapes => [...prevShapes, newRectangle]);
      }
    }

    // Close modal
    setModalOpen(false);
  };

  // Function to handle grouping of selected shapes
  const handleGroupShapes = () => {
    const groupedShape = {
      type: 'group',
      shapes: selectedShapes,
    };

    setShapes([...shapes, groupedShape]);
    setSelectedShapes([]);
  };

  return (
    <div className="App" onMouseMove={handleMouseMove}>
      <h1>Shape Editor</h1>
      <div className="toolbar">
        <button onClick={() => handleToolSelect('rectangle')} disabled={!!drawingShape}>Draw Rectangle</button>
        <button onClick={() => handleToolSelect('table')} disabled={!!drawingShape}>Insert Table</button>
        <button onClick={handleGroupShapes} disabled={selectedShapes.length === 0}>Group Shapes</button>
      </div>
      <div className="canvas" onClick={handleCanvasClick}>
        {drawingShape && (
          <div
            className="temp-shape"
            style={{
              left: Math.min(drawingShape.startX, drawingShape.endX),
              top: Math.min(drawingShape.startY, drawingShape.endY),
              width: Math.abs(drawingShape.endX - drawingShape.startX),
              height: Math.abs(drawingShape.endY - drawingShape.startY),
            }}
          />
        )}
        {shapes.map((shape, index) => (
          <div
            key={index}
            className={`shape ${shape.type === 'table' ? 'table' : ''} ${selectedShapes.includes(index) ? 'selected' : ''}`}
            style={{ left: shape.left, top: shape.top, width: shape.width, height: shape.height }}
            onMouseDown={(event) => handleShapeDrag(event, index)}
            onClick={(event) => {
              if (event.shiftKey) {
                // Shift 키를 누르면 복수 선택 가능
                setSelectedShapes(prevSelectedShapes => {
                  if (prevSelectedShapes.includes(index)) {
                    return prevSelectedShapes.filter(i => i !== index);
                  } else {
                    return [...prevSelectedShapes, index];
                  }
                });
              } else {
                // Shift 키를 누르지 않은 경우 단일 선택
                setSelectedShapes([index]);
              }
            }}
          />
        ))}
      </div>

      {/* Modal for creating table */}
      {modalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={handleModalClose}>&times;</span>
            <h2>Create Table</h2>
            <label>
              Rows:
              <input type="number" value={numRows} min="1" onChange={(e) => setNumRows(parseInt(e.target.value))} />
            </label>
            <label>
              Columns:
              <input type="number" value={numColumns} min="1" onChange={(e) => setNumColumns(parseInt(e.target.value))} />
            </label>
            <button onClick={handleTableCreate}>Create Table</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
