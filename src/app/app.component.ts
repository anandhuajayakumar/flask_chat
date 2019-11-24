import { Component, OnInit } from '@angular/core';
import { SocketService } from './services/socket.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'flaskChat';

  constructor(
    private socket: SocketService
  ) { }

  ngOnInit() {
    this.socket.sendMessage('a');
  }
}
