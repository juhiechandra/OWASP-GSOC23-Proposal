import { useState, useEffect } from 'react';

function ScanCounter({ duration }) {
  const [remainingTime, setRemainingTime] = useState(duration * 60);

  useEffect(() => {
    const interval = setInterval(() => {
      setRemainingTime((prevTime) => prevTime - 1);
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  };

  return (
    <div>
      <p>Remaining Time: {formatTime(remainingTime)}</p>
    </div>
  );
}


<ScanCounter duration={scanDuration} />
