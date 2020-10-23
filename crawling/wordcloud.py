import stylecloud

font_location = 'SeoulNamsanB.ttf'

stylecloud.gen_stylecloud(file_path='noun_list_environment.csv',
                          icon_name='fab fa-envira',
                          palette='colorbrewer.sequential.Greens_9',
                          background_color='white',
                          gradient='horizontal',
                          font_path=font_location,
                          output_name='environment.png'
                          )