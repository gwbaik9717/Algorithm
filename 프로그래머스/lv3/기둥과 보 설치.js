function solution(n, orders) {
    const answer = [];
    const board = Array.from({length: n+1}, () => Array.from({length: n+1}, () => []))
    
    // 전체 확인
    const check = () => {
        for (let i=0; i<=n; i++){
            for (let j=0; j <=n; j++){
                for (let k=0; k < 2; k++){
                    if (board[i][j].includes(k)){
                      // 기둥
                      if (k === 0){
                          if (i === 0){
                              continue
                          }
                          
                          if (i >= 1 && board[i-1][j].includes(k)){
                              continue
                          }
                          
                          if (board[i][j].includes(1)){
                              continue
                          }
                          
                          if (j>=1 && board[i][j-1].includes(1)){
                              continue
                          }
                          
                          return false
                      }  
                        
                      // 보
                      if (j>=1 && j < n && board[i][j-1].includes(1) && board[i][j+1].includes(1)){
                          continue
                      }
                      
                      if (i>=1 && board[i-1][j].includes(0)){
                          continue
                      }
                        
                      if (i>=1 && j<n && board[i-1][j+1].includes(0)){
                          continue
                      }
                        
                      return false
                    }
                }
            }
        }
        
        return true
    }
    
    for (const order of orders){
        
        const [x, y, a, b] = order
        
        // 삭제
        if (b === 0){
            board[y][x] = board[y][x].filter(item => item !== a)
            if (!check()){
                board[y][x].push(a)
            }
            
            continue
        }
        
        // 설치
        board[y][x].push(a)
        if (!check()){
            board[y][x] = board[y][x].filter(item => item !== a)
        }
    }
    
    for (let x=0; x<=n; x++){
        for (let y=0; y<=n; y++){
            
            for (let k=0; k<2; k++){
                if (board[y][x].includes(k)){
                    answer.push([x, y, k])
                }
                
            }
        }
    }
    
    return answer;
}