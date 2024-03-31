import { json } from '@sveltejs/kit';
import fs from 'fs/promises';
import path from 'path';

export async function POST(request: any) {
  try {
    
  } catch (error) {
    console.error('Error:', error);
    return json({ error: '서버 오류' }, { status: 500 });
  }
}
