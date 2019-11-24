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
  ) {
    this.socket.getMessages().subscribe(
      data => {
        console.log(data);
      }
    );
  }

  ngOnInit() {
    this.socket.sendMessage({
      content: 'aaa',
      user: '1',
      chat: 'main'
    });
  }
}
