import React, { useRef } from "react";
import Webcam from "react-webcam";
import fetch from "isomorphic-fetch";

function Camera() {
  const webcamRef = useRef(null);

  const capture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    console.log(imageSrc);

    fetch("http://127.0.0.1:5000/api/upload", {
      method: "POST",
      body: JSON.stringify({ image: imageSrc }),
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error(error));
  };

  return (
    <div>
      <Webcam audio={false} ref={webcamRef} />
      <button onClick={capture}>Capture photo</button>
    </div>
  );
}

export default Camera;
