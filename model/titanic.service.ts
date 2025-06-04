import path from 'path';
import { execFile } from 'child_process';
import { promisify } from 'util';
import { TitaticDto } from './titanic.dto';

const execFileAsync = promisify(execFile);

const titanic = async (data: TitaticDto): Promise<{ prediction: number }> => {
  const dataJson = JSON.stringify(data);

  // Como están en la misma carpeta solo unimos __dirname con 'predict.py'
  const scriptPath = path.join(__dirname, 'predict.py');

  const { stdout } = await execFileAsync('python', [scriptPath, dataJson]);

  const result = JSON.parse(stdout);
  return { prediction: result.prediction };
};

export {
  titanic
};
