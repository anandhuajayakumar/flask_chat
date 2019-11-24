import { Injectable } from '@angular/core';
import * as io from 'socket.io-client';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SocketService {
  private socket;

  constructor() {
    this.socket = io(environment.serverUrl);
    this.socket.on('connect', () => {
      this.socket.emit('my event', {
        data: 'User Connected'
      });
    });
  }

  public sendMessage(message) {
    this.socket.emit('new-message', message);
  }

  public getMessages = () => {
    return Observable.create(observer => {
      this.socket.on('response', message => {
        observer.next(message);
      });
    });
  }
}
