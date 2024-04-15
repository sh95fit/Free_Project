import React, { useState } from 'react';
import './App.css';

function App() {
  const [selectedTool, setSelectedTool] = useState(null);
  const [drawingShape, setDrawingShape] = useState(null);
  const [shapes, setShapes] = useState([]);

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

  return (
    <div className="App" onMouseMove={handleMouseMove}>
      <h1>Shape Editor</h1>
      <div className="toolbar">
        <button onClick={() => handleToolSelect('rectangle')} disabled={!!drawingShape}>Draw Rectangle</button>
        <button onClick={() => handleToolSelect('icon')}>Insert Icon</button>
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
            className="shape"
            style={{ left: shape.left, top: shape.top, width: shape.width, height: shape.height }}
            onMouseDown={(event) => handleShapeDrag(event, index)}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
