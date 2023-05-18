import React, { useRef } from "react";
import Webcam from "react-webcam";
import fetch from "isomorphic-fetch";
import "./Camera.css";

function Camera() {
  const webcamRef = useRef(null);

  const capture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    console.log(imageSrc);

    fetch(
      "https://166a-2405-4802-8119-edd0-9c82-3d30-eafc-b229.ngrok-free.app/api/upload",
      {
        method: "POST",
        body: JSON.stringify({ image: imageSrc }),
        headers: { "Content-Type": "application/json" },
      }
    )
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  };

  return (
    <div className="camera-wrapper">
      <Webcam audio={false} ref={webcamRef} className="webcam" />
      <button onClick={capture} className="capture-button">
        {" "}
        Capture photo{" "}
      </button>{" "}
    </div>
  );
}

export default Camera;
