import React, { useState } from "react";
import axios from "axios";
import WebcamCapture from "./WebcamCapture";

const App = () => {
  const [image, setImage] = useState(null);

  const handleImageCapture = (imgSrc) => {
    setImage(imgSrc);
  };

  const sendImageToServer = async () => {
    try {
      let res = await axios.post("http://127.0.0.1:5000/api", { image: image });
      console.log(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <WebcamCapture onCapture={handleImageCapture} />
      <button onClick={sendImageToServer}>Gửi ảnh</button>
    </div>
  );
};

export default App;
