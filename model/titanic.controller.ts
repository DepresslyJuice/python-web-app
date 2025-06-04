import { Request, Response } from 'express';
import * as TitanicService from './titanic.service';
import { TitaticDto } from './titanic.dto';

const predictTitanic = async (req: Request, res: Response) => {
  try {
    const inputData: TitaticDto = req.body;
    const result = await TitanicService.titanic(inputData);
    res.json(
      {
        success: true,
        prediction: result.prediction
      });
  } catch (error) {
    console.error('Error en predicción:', error);
    res.status(500).json({ success: false, message: 'Error en la predicción' });
  }
};

export {
  predictTitanic
};