import { Injectable } from '@angular/core';
import * as io from 'socket.io-client';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SocketService {
  private socket;

  constructor() {
    // this.socket = io('/test');
    this.socket = io('localhost:5000'); // i tried this
    // this.socket = io(`/api`); // i also tried this

  }

  public sendMessage(message) {
    this.socket.emit('new-message', message);
  }

  public getMessages = () => {
    return Observable.create(observer => {
      this.socket.on('new-message', message => {
        observer.next(message);
      });
    });
  }
}
