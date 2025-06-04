import { Router } from 'express';
import * as titanicController from './titanic.controller';

const router = Router();

// Ruta POST para predecir
router.post('/predict', titanicController.predictTitanic);

export default router;
