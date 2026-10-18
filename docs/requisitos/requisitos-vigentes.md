# Requisitos vigentes do Roomy (extraídos do documento PI 2º período, Fase 02)

Fonte de verdade: o documento de especificação. Em caso de divergência, vale o documento.

13 REGRAS DE NEGÓCIO

 Criação obrigatória: 1º Período – Fase 02

 Atualização: contínua.

As regras de negócio definem as políticas, restrições e condições que regem o funcionamento do Roomy dentro do domínio do problema. Elas são independentes de tecnologia e estabelecem o comportamento esperado da plataforma, servindo de base para a definição dos requisitos funcionais e não funcionais. As regras a seguir foram levantadas a partir dos problemas identificados no mercado de locação residencial e das necessidades do público-alvo: jovens e universitários entre 18 e 30 anos que buscam moradia com mais transparência, flexibilidade e segurança.

RNE-001 – Cadastro obrigatório para acesso às funcionalidades completas

| ID | Descrição | Requisitos Relacionados |
| RNE-001 | Somente usuários com cadastro ativo e perfil minimamente preenchido (nome, e-mail confirmado e tipo de conta) podem acessar os detalhes completos dos imóveis, iniciar contato com anunciantes e utilizar o sistema de match. | RF-001 |
| | | |
| | Usuários não autenticados visualizam uma listagem resumida de imóveis, sem acesso a endereço completo, fotos adicionais, contato do anunciante ou funcionalidades interativas. | RF-002 |
| | | |
| | | RF-006 |
| | | |
| | | RF-007 |
| | | |
| | | RF-009 |
| | | |
| | | RNF-004 |
| Detalhamento: Exigir cadastro protege os dados dos anunciantes e garante rastreabilidade nas interações. Sem conta, o usuário não pode contatar proprietários nem participar do match, pois essas ações envolvem troca de informações pessoais. O perfil mínimo é nome, e-mail verificado e tipo de conta; perfis incompletos navegam, mas são avisados a concluir o cadastro. | | |

RNE-002 – Informações mínimas obrigatórias em todo anúncio

| ID | Descrição | Requisitos Relacionados |
| RNE-002 | Todo anúncio publicado na plataforma deve conter obrigatoriamente: valor mensal do aluguel, localização (bairro e cidade), tipo de imóvel, número de quartos disponíveis, prazo mínimo de contrato e ao menos uma foto do imóvel. | RF-004 |
| | | |
| | O sistema deve impedir a publicação de anúncios enquanto algum campo obrigatório não estiver preenchido. | RF-005 |
| | | |
| | | RNF-002 |
| | | |
| | | RNF-001 |
| Detalhamento: A falta de padronização nos anúncios gera perda de tempo para ambos os lados e abre espaço para mal-entendidos e fraude. Com campos obrigatórios, qualquer anúncio publicado já traz o mínimo para o locatário avaliar o imóvel antes de fazer contato. Campos em branco ou respostas genéricas como "a combinar" não são aceitos. | | |

RNE-003 – Transparência obrigatória nas condições contratuais

| ID | Descrição | Requisitos Relacionados |
| RNE-003 | As condições do contrato de locação, incluindo prazo mínimo de permanência e regras de cancelamento antecipado, devem ser exibidas de forma clara, em linguagem acessível, na página de cada imóvel, antes de qualquer contato entre locatário e anunciante. | RF-004 |
| | | |
| | Não é permitido omitir, deixar em branco ou usar termos vagos nos campos referentes a prazo mínimo e penalidades por saída antecipada. | RF-005 |
| | | |
| | | RNF-002 |
| Detalhamento: Contratos com prazo mínimo longo (usualmente 30 meses, conforme art. 46 da Lei 8.245/91) e condições de rescisão pouco claras prendem jovens a situações que podem não caber mais em sua realidade, muitas vezes sem que percebam isso antes de assinar. O Roomy combate isso tornando essas condições de preenchimento obrigatório e exibindo-as em linguagem simples, com termos jurídicos evitados ou acompanhados de explicação. | | |

RNE-004 – Separação entre perfil de locatário e perfil de anunciante

| ID | Descrição | Requisitos Relacionados |
| RNE-004 | O sistema deve distinguir dois tipos de conta: locatário (usuário que busca moradia) e anunciante (proprietário ou responsável pelo imóvel). Cada tipo de conta tem acesso a funcionalidades específicas e exclusivas. | RF-001 |
| | | |
| | Um mesmo usuário pode possuir os dois tipos de perfil, desde que os identifique no momento do cadastro ou posteriormente nas configurações da conta. | RF-002 |
| | | |
| | | RF-004 |
| | | |
| | | RNF-004 |
| Detalhamento: A separação de perfis faz o sistema exibir as funcionalidades certas para cada usuário: o anunciante precisa de painel de imóveis, histórico de contatos e edição de anúncios; o locatário, de busca, filtros, match e contato. Misturar tudo em um único tipo de conta tornaria a interface confusa. | | |

RNE-005 – Controle do anunciante sobre seus próprios anúncios

| ID | Descrição | Requisitos Relacionados |
| RNE-005 | O anunciante tem controle total sobre seus anúncios e pode editá-los, desativá-los ou reativá-los a qualquer momento. | RF-004 |
| | | |
| | Anúncios desativados não aparecem nos resultados de busca para locatários. O histórico do anúncio é mantido internamente para fins de rastreabilidade da plataforma. | RF-005 |
| | | |
| | | RNF-003 |
| Detalhamento: Anúncios de imóveis indisponíveis geram frustração para o locatário e contatos desnecessários para o anunciante. O controle de visibilidade mantém a listagem fiel à realidade do mercado. O histórico interno preserva as avaliações vinculadas ao imóvel após a desativação e serve para auditoria e resolução de disputas. | | |

RNE-006 – Sistema de match baseado em interesse mútuo e dados declarados

| ID | Descrição | Requisitos Relacionados |
| RNE-006 | O sistema de compatibilidade para busca de colegas de quarto deve funcionar exclusivamente com base em informações declaradas voluntariamente pelo próprio usuário. O contato entre dois usuários pelo sistema de match só é liberado quando ambos demonstrarem interesse mútuo. | RF-008 |
| | | |
| | O sistema não pode inferir, compartilhar ou expor informações do usuário sem seu consentimento explícito. | RF-009 |
| | | |
| | | RNF-004 |
| | | |
| | | RNF-001 |
| Detalhamento: O match, isoladamente, não é exclusividade do Roomy — plataformas como Roomgo e WebQuarto já conectam colegas de quarto no mercado brasileiro (ver §10). O diferencial do Roomy está em combinar esse match com a padronização obrigatória das condições contratuais do imóvel (RNE-002, RNE-003), algo que essas soluções não fazem. Dentro dessa combinação, o match permite que jovens sem condição de arcar sozinhos com a moradia encontrem colegas de quarto com rotinas compatíveis. O modelo de interesse mútuo protege a privacidade e evita constrangimentos — o contato só é liberado após confirmação dos dois lados, e quem não é escolhido não recebe notificação. | | |

RNE-007 – Proteção de dados pessoais até confirmação de interesse

| ID | Descrição | Requisitos Relacionados |
| RNE-007 | Dados pessoais de contato dos usuários, como telefone, e-mail particular e endereço residencial, não devem ser expostas publicamente na plataforma nem compartilhadas automaticamente com outros usuários. | RF-007 |
| | | |
| | O compartilhamento de contato direto deve ser uma ação voluntária do próprio usuário, realizada após o estabelecimento de comunicação inicial pelo canal interno da plataforma. | RF-009 |
| | | |
| | | RNF-004 |
| Detalhamento: Expor telefone ou e-mail publicamente, numa plataforma que conecta desconhecidos, pode gerar assédio, spam ou uso indevido das informações. O Roomy atua como intermediário nas fases iniciais do contato, liberando dados pessoais apenas quando o próprio usuário decide compartilhá-los. | | |

RNE-008 – Avaliações públicas e protegidas contra remoção pelo avaliado

| ID | Descrição | Requisitos Relacionados |
| RNE-008 | Após ambas as partes confirmarem na plataforma que a locação foi concretizada, locatário e proprietário podem avaliar a experiência com uma nota de 1 a 5 e um comentário descritivo. Uma vez publicada, a avaliação não pode ser removida ou editada pelo usuário avaliado. | RF-012 |
| | | |
| | Contestações de avaliações consideradas indevidas devem ser realizadas exclusivamente pelo canal de suporte da plataforma. | RF-014 |
| | | |
| | | RNF-003 |
| | | |
| | | RNF-004 |
| Detalhamento: As avaliações constroem confiança entre os usuários: saber que um proprietário é bem avaliado por inquilinos anteriores, ou um locatário por quem já alugou para ele, reduz a insegurança nas negociações. A proteção contra remoção pelo avaliado impede que registros negativos sejam apagados; avaliações falsas ou ofensivas podem ser contestadas pelo suporte. | | |

RNE-009 – Comparativo de valores baseado nos anúncios da própria plataforma

| ID | Descrição | Requisitos Relacionados |
| RNE-009 | O sistema deve oferecer ao locatário uma referência comparativa do valor do aluguel de um imóvel em relação aos anúncios semelhantes disponíveis na mesma localização e com características similares. | RF-011 |
| | | |
| | A comparação deve ser apresentada de forma visual e simples, indicando se o valor está abaixo, dentro ou acima da média dos imóveis cadastrados na plataforma para aquela categoria e região. | RNF-002 |
| Detalhamento: Um dos objetivos centrais do Roomy, citado na descrição do produto, é oferecer "comparativos visuais de valores" para reduzir a assimetria de informação entre locador e locatário. Esta regra garante que a funcionalidade seja construída com os dados da própria plataforma, sem integrações externas neste primeiro momento. | | |

14 REQUISITOS FUNCIONAIS

 Criação obrigatória: 1º Período – Fase 02

 Atualização: contínua.

Os requisitos funcionais descrevem o que o sistema Roomy deve permitir que os usuários realizem. Cada requisito foi definido a partir dos problemas identificados, das regras de negócio estabelecidas na seção anterior e das necessidades do público-alvo. Neste primeiro período, os requisitos são apresentados de forma conceitual, sem detalhamento técnico de implementação. O foco está nas necessidades do usuário e no comportamento esperado do sistema.

RF-001 – Cadastro de novo usuário

| ID | Descrição | Status | Prioridade |
| RF-001 | O sistema deve permitir que qualquer pessoa crie uma conta informando nome completo, endereço de e-mail, senha e o tipo de conta desejado (locatário ou anunciante). | Levantado | Alta |
| | | | |
| | O e-mail informado deve ser único no sistema. O usuário deve confirmar o endereço de e-mail por meio de um link enviado ao e-mail cadastrado antes de acessar as funcionalidades completas da plataforma. | | |
| Detalhamento: O cadastro é a porta de entrada para todas as funcionalidades e liga-se à RNE-001 e à RNE-004. Deve ser simples e rápido, sem campos que desestimulem o primeiro acesso. A confirmação por e-mail reduz o risco de perfis falsos, e o tipo de conta escolhido define as funcionalidades exibidas na sequência. | | | |

RF-002 – Login e encerramento de sessão

| ID | Descrição | Status | Prioridade |
| RF-002 | O sistema deve permitir que usuários cadastrados realizem login com e-mail e senha para acessar as funcionalidades completas da plataforma. | Levantado | Alta |
| | | | |
| | O usuário deve poder encerrar sua sessão (logout) a qualquer momento. A sessão deve permanecer ativa por tempo suficiente para evitar desconexões automáticas frequentes durante o uso, especialmente em dispositivos móveis. | | |
| Detalhamento: O acesso autenticado permite ao sistema identificar o usuário e exibir as funcionalidades do seu tipo de conta, conforme a RNE-004. Manter a sessão ativa por período razoável importa para um público que usa a plataforma em deslocamento e retoma o uso após intervalos. | | | |

RF-003 – Recuperação de senha

| ID | Descrição | Status | Prioridade |
| RF-003 | O sistema deve permitir que o usuário recupere o acesso à sua conta caso esqueça a senha, por meio do envio de um link de redefinição para o e-mail cadastrado. | Levantado | Alta |
| | | | |
| | O usuário também deve poder alterar sua senha a partir das configurações da conta, desde que informe a senha atual. | | |
| Detalhamento: Sem recuperação de senha, o usuário que esquece a sua perde o acesso a anúncios, conversas e avaliações. O processo deve ser simples e confiável pelo e-mail cadastrado, e a alteração de senha nas configurações permite manter a conta segura de forma proativa. | | | |

RF-004 – Publicação de anúncio de imóvel

| ID | Descrição | Status | Prioridade |
| RF-004 | O sistema deve permitir que usuários com conta do tipo anunciante publiquem anúncios de imóveis disponíveis para locação, preenchendo todos os campos obrigatórios definidos na RNE-002 e as condições contratuais exigidas pela RNE-003. | Levantado | Alta |
| | | | |
| | O anúncio só deve ser publicado e exibido nos resultados de busca após a validação de que todos os campos obrigatórios foram preenchidos corretamente. | | |
| Detalhamento: A publicação de anúncios é a principal funcionalidade do lado do anunciante. O sistema deve validar os campos obrigatórios antes de confirmar, com mensagem clara em caso de campos incompletos, e permitir que o anunciante visualize o anúncio como o locatário o veria antes de receber contatos. | | | |

RF-005 – Edição, desativação e reativação de anúncio pelo anunciante

| ID | Descrição | Status | Prioridade |
| RF-005 | O sistema deve permitir que o anunciante edite as informações de um anúncio já publicado, desative o anúncio quando o imóvel não estiver mais disponível para locação, ou reative um anúncio previamente desativado. | Levantado | Alta |
| | | | |
| | Anúncios desativados não devem aparecer nos resultados de busca para locatários, conforme RNE-005. | | |
| Detalhamento: Anúncios desatualizados prejudicam o locatário e geram contatos desnecessários ao anunciante. A edição permite atualizar valores, fotos e condições sempre que necessário; a desativação, acessível no painel, evita que imóveis já alugados continuem aparecendo como disponíveis; e a reativação permite que o anunciante volte a divulgar um imóvel que ficou temporariamente indisponível, sem precisar recriar o anúncio do zero. | | | |

RF-006 – Busca e filtragem de imóveis disponíveis

| ID | Descrição | Status | Prioridade |
| RF-006 | O sistema deve oferecer uma ferramenta de busca de imóveis com filtros por: localização (cidade e/ou bairro), valor máximo de aluguel, tipo de imóvel, número de quartos e prazo mínimo de contrato. | Levantado | Alta |
| | | | |
| | Os resultados devem exibir apenas anúncios ativos que correspondam aos critérios selecionados pelo usuário. | | |
| Detalhamento: A busca com filtros é o caminho principal do locatário até o imóvel. O filtro por prazo mínimo é especialmente relevante, pois permite localizar imóveis com condições mais flexíveis — um dos problemas centrais identificados na seção 2.2. Os filtros devem exigir o mínimo de digitação em dispositivos móveis. | | | |

RF-007 – Visualização detalhada de imóvel

| ID | Descrição | Status | Prioridade |
| RF-007 | O sistema deve exibir uma página dedicada a cada imóvel anunciado, contendo todas as informações do anúncio: fotos, descrição completa, valor do aluguel, localização, prazo mínimo e condições de cancelamento do contrato. | Levantado | Alta |
| | | | |
| | A página detalhada — com fotos, descrição completa, endereço completo e acesso ao canal de mensagens do anunciante — é exibida somente a usuários autenticados; usuários não autenticados visualizam apenas a listagem resumida, conforme RNE-001. Telefone e e-mail do anunciante não são exibidos automaticamente, conforme RNE-007. | | |
| Detalhamento: É na página de detalhes que o locatário decide se entra em contato. Ela deve organizar as informações com clareza, especialmente as condições contratuais exigidas pela RNE-003. Restringir o contato do anunciante a usuários autenticados alinha-se à RNE-001 e mantém o Roomy como intermediário nas etapas iniciais. | | | |

RF-008 – Preenchimento do perfil de convivência para o sistema de match

| ID | Descrição | Status | Prioridade |
| RF-008 | O sistema deve permitir que locatários preencham informações sobre seu estilo de vida e hábitos de convivência, como horário de sono, nível de organização, tolerância a barulho, animais de estimação e frequência de visitas de pessoas. | Levantado | Média |
| | | | |
| | O preenchimento dessas informações é voluntário e pode ser editado ou removido pelo usuário a qualquer momento, conforme RNE-006. | | |
| Detalhamento: O perfil de convivência é pré-requisito para o match, e quanto mais completo, melhores as sugestões. Por ser voluntário, o preenchimento deve ser incentivado sem bloqueios. A edição livre permite manter o perfil atualizado conforme a rotina do usuário muda. | | | |

RF-009 – Sistema de match para busca de colegas de quarto

| ID | Descrição | Status | Prioridade |
| RF-009 | O sistema deve sugerir perfis de usuários compatíveis para divisão de moradia, com base nas informações declaradas no perfil de convivência. O contato entre dois usuários só deve ser liberado após demonstração de interesse mútuo pelos dois lados. | Levantado | Média |
| | | | |
| | O usuário que não demonstrou interesse no outro não deve ser notificado caso seja desconsiderado, conforme RNE-006. | | |
| Detalhamento: O diferencial do Roomy não é o match isolado — soluções como Roomgo e WebQuarto já resolvem parte desse problema no Brasil (ver §10) —, mas a combinação entre match de convivência e padronização obrigatória das condições contratuais do imóvel, ausente nas soluções existentes. O match resolve o problema de jovens que precisam dividir moradia mas não têm como encontrar colegas com hábitos compatíveis. O modelo de interesse mútuo protege a privacidade, e a ausência de notificação em caso de recusa reduz desconfortos sociais. | | | |

RF-010 – Canal de contato interno entre locatário e anunciante

| ID | Descrição | Status | Prioridade |
| RF-010 | O sistema deve disponibilizar um canal de mensagens interno para que locatários interessados em um imóvel possam entrar em contato com o anunciante diretamente pela plataforma, sem necessidade de expor dados pessoais de imediato. | Levantado | Alta |
| | | | |
| | O canal deve estar acessível na página de detalhes do imóvel e disponível apenas para usuários autenticados, conforme RNE-001 e RNE-007. | | |
| Detalhamento: O canal interno protege a privacidade nas etapas iniciais da negociação, conforme a RNE-007: locatário e anunciante alinham detalhes do imóvel antes de decidirem compartilhar telefone ou e-mail pessoal. A comunicação mediada também facilita identificar comportamentos inadequados. | | | |

RF-011 – Comparativo de valores de aluguel

| ID | Descrição | Status | Prioridade |
| RF-011 | O sistema deve exibir, na página de detalhes de cada imóvel, uma referência comparativa do valor do aluguel em relação à média dos imóveis semelhantes disponíveis na mesma localização e categoria. | Levantado | Média |
| | | | |
| | A comparação deve ser apresentada de forma visual e simples, indicando se o valor está abaixo, dentro ou acima da média dos anúncios da própria plataforma para aquela região e tipo de imóvel, conforme RNE-009. | | |
| Detalhamento: Este requisito realiza uma das características centrais citadas na descrição do produto: oferecer "comparativos visuais de valores" para reduzir a assimetria de informação. Sem pesquisar em outras plataformas, o locatário avalia rapidamente se o preço é justo para aquela localização e tipo de imóvel, com base nos próprios anúncios do Roomy. | | | |

RF-012 – Avaliação de locatário e proprietário

| ID | Descrição | Status | Prioridade |
| RF-012 | O sistema deve permitir que usuários avaliem uma experiência de locação após ambas as partes confirmarem que ela foi concretizada, conforme o RF-014. Ambas podem avaliar independentemente, atribuindo nota de 1 a 5 e comentário descritivo. | Levantado | Média |
| | | | |
| | As avaliações devem ficar visíveis nos perfis dos avaliados e não podem ser removidas pelo avaliado, conforme RNE-008. | | |
| Detalhamento: As avaliações públicas constroem a reputação dos usuários e servem de referência para futuras negociações: um locatário bem avaliado aluga novamente com mais facilidade, e um proprietário bem avaliado atrai mais interessados. A proteção contra remoção pelo avaliado mantém o histórico confiável. | | | |

RF-013 – Gerenciamento do perfil pelo usuário

| ID | Descrição | Status | Prioridade |
| RF-013 | O sistema deve permitir que o usuário edite as informações do seu perfil a qualquer momento, incluindo foto, nome de exibição, breve descrição pessoal e dados de contato visíveis para outros usuários. | Levantado | Média |
| | | | |
| | O usuário também deve poder alterar sua senha e gerenciar as informações do perfil de convivência (para locatários) ou do perfil de anunciante, de forma independente das informações do perfil geral. | | |
| Detalhamento: O perfil é a identidade do usuário na plataforma — importa para o locatário que quer se apresentar bem a proprietários e possíveis colegas de quarto, e para o anunciante que precisa transmitir credibilidade. A separação entre perfil geral e perfil de convivência acompanha a divisão de responsabilidades da RNE-004. | | | |

RF-014 – Confirmação de locação concretizada

| ID | Descrição | Status | Prioridade |
| RF-014 | O sistema deve permitir que locatário e anunciante registrem, a partir da conversa referente ao imóvel, que a locação foi concretizada. A confirmação de ambas as partes libera a avaliação mútua prevista no RF-012. | Levantado | Alta |
| | | | |
| | Enquanto apenas uma das partes tiver confirmado, a avaliação permanece indisponível. O registro não envolve valores, prazos ou assinatura de contrato: serve apenas como marco que vincula a avaliação a uma locação real. | | |
| Detalhamento: Sem um marco que vincule a avaliação a uma locação real, qualquer par de usuários que apenas trocou mensagens poderia avaliar o outro, o que enfraqueceria a credibilidade das notas exibidas nos perfis. A confirmação por ambas as partes é o mecanismo mais simples de garantir esse vínculo sem exigir gestão de contratos, atendendo à RNE-008. | | | |

15 REQUISITOS NÃO FUNCIONAIS

 Criação obrigatória: 1º Período – Fase 02

 Atualização: contínua.

Os requisitos não funcionais definem como o sistema Roomy deve se comportar, quais restrições deve respeitar e quais características de qualidade deve atender, independentemente das funcionalidades. Neste primeiro período, esses requisitos são apresentados de forma descritiva e em linguagem acessível, com base no perfil do público-alvo, nos problemas identificados e nas características esperadas de uma plataforma confiável e segura para o segmento de locação residencial.

RNF-001 – Usabilidade

| ID | Descrição | Status | Prioridade |
| RNF-001 | As principais funcionalidades devem ser acessadas sem exigir conhecimento técnico ou experiência prévia com plataformas de aluguel. Métricas: (1) as tarefas principais — buscar um imóvel, publicar um anúncio e iniciar uma conversa — devem ser concluídas em no máximo 4 interações a partir da tela inicial; (2) botões e áreas tocáveis devem ser grandes o suficiente para acionamento com o dedo, sem necessidade de ampliar a tela; (3) nenhuma tela deve exigir rolagem horizontal. | Levantado | Alta |
| | | | |
| | Os textos devem ser legíveis e o fluxo de navegação deve ser previsível e consistente em todas as telas. | | |
| Detalhamento: O público-alvo usa a plataforma principalmente pelo celular, em deslocamento e com atenção reduzida. Nesse contexto, fluxos com muitos passos, menus confusos ou terminologia técnica aumentam o abandono, por isso a interface deve exigir o mínimo de esforço nas ações principais. | | | |

RNF-002 – Transparência e clareza das informações

 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ID Descrição Status Prioridade
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ ---------------
 RNF-002 As informações dos imóveis anunciados devem ser apresentadas em linguagem clara e acessível, sem termos ambíguos, informações ocultas ou linguagem jurídica de difícil compreensão. Métricas: (1) os campos de valor do aluguel, prazo mínimo e condições de cancelamento devem estar visíveis sem necessidade de rolagem na página de detalhes do imóvel; (2) nenhum campo obrigatório pode conter o texto “a combinar” ou equivalente vago. Levantado Alta

 Detalhamento: A falta de transparência é o principal problema que o Roomy se propõe a combater. Exibir informações incompletas contraria o propósito da plataforma. Cláusulas devem ser resumidas em linguagem simples, e encargos ou taxas informados no próprio anúncio, evitando surpresas ao locatário após o contato.
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

RNF-003 – Confiabilidade

| ID | Descrição | Status | Prioridade |
| RNF-003 | O sistema deve funcionar de maneira estável, sem erros frequentes ou comportamentos inesperados. Métrica: nenhuma ação do usuário deve resultar em perda de dados já preenchidos sem aviso prévio. | Levantado | Alta |
| | | | |
| | Ações importantes como publicar um anúncio, enviar uma mensagem ou registrar uma avaliação devem ser confirmadas visualmente ao usuário para que ele saiba que foram realizadas com sucesso. O feedback visual deve aparecer em até 2 segundos após a ação. | | |
| Detalhamento: Falhas frequentes prejudicam a credibilidade da plataforma e podem custar ao usuário um anúncio em publicação, uma mensagem não entregue ou uma avaliação perdida. A confirmação visual reduz a insegurança e evita que ele repita ações sem saber se a anterior funcionou. | | | |

RNF-004 – Segurança e proteção de dados

| ID | Descrição | Status | Prioridade |
| RNF-004 | Dados pessoais e credenciais, como senha, telefone e endereço particular, não devem ser expostos a outros usuários sem consentimento explícito. Métricas: (1) senhas nunca armazenadas em texto legível, passando por criptografia antes de serem salvas; (2) toda comunicação entre navegador e servidor deve usar conexão segura (HTTPS); (3) dados sensíveis não devem aparecer em registros de erro do sistema; (4) sessões expiram após 7 dias de inatividade. | Levantado | Alta |
| | | | |
| | O acesso ao sistema deve ser feito por autenticação com e-mail e senha. | | |
| Detalhamento: Por conectar pessoas para fins de moradia compartilhada, o Roomy lida com dados pessoais cuja exposição pode gerar assédio ou risco à segurança, e os usuários precisam confiar que não serão expostos a terceiros. A proteção de senhas é requisito básico desde o início, e a restrição de dados a usuários não autenticados alinha-se à RNE-001 e à RNE-007. | | | |

RNF-005 – Desempenho

| ID | Descrição | Status | Prioridade |
| RNF-005 | O sistema deve responder às ações do usuário sem demoras perceptíveis. Métricas: (1) carregamento inicial de páginas em até 3 segundos em conexão móvel comum; (2) resultados de busca exibidos em até 2 segundos após aplicação dos filtros; (3) envio de mensagem confirmado em até 1 segundo. | Levantado | Alta |
| | | | |
| | Imagens dos anúncios devem ser carregadas de forma otimizada para não comprometer o desempenho em conexões de dados móveis. Métrica: cada imagem de anúncio deve ter tamanho máximo de 500 KB após compressão automática pelo sistema. | | |
| Detalhamento: Com uso predominante em celular e conexão de dados móveis, páginas pesadas e imagens não otimizadas tornam a plataforma lenta e aumentam o abandono. Tratar isso desde o início evita retrabalho nos períodos seguintes. | | | |

RNF-006 – Compatibilidade Multiplataforma e Responsividade

 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ID Descrição Status Prioridade
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ ---------------
 RNF-006 O sistema deve funcionar corretamente nos principais navegadores (Chrome, Firefox e Safari) em dispositivos móveis (Android e iOS) e em desktops, sem perda de funcionalidade ou necessidade de configuração especial por parte do usuário. A interface deve ser responsiva, adaptando-se automaticamente a diferentes tamanhos de tela. Métricas: (1) funcional nos navegadores mais utilizados (Chrome, Firefox e Safari); (2) layout adaptado tanto a telas de celular quanto de computador; (3) nenhum elemento de interface deve sobrepor outro ou sair da área visível em telas pequenas. Levantado Alta

 Detalhamento: Como o público-alvo acessa majoritariamente pelo celular, a aplicação precisa funcionar bem em telas pequenas, sem exigir zoom ou rolagem horizontal. O suporte aos principais navegadores garante acesso independentemente do dispositivo ou sistema operacional.
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

RNF-007 – Disponibilidade

| ID | Descrição | Status | Prioridade |
| RNF-007 | O sistema deve estar disponível para acesso pela maior parte do tempo, especialmente nos períodos de maior uso esperado pelo público-alvo, como noites e fins de semana. Métricas: (1) disponibilidade mínima de 99% mensal; (2) em caso de manutenção planejada, o sistema deve exibir aviso ao usuário com até 24 horas de antecedência. | Levantado | Alta |
| | | | |
| | Interrupções planejadas para manutenção devem ser comunicadas aos usuários com antecedência, sempre que possível. | | |
| Detalhamento: Quem busca moradia antes de uma mudança precisa do sistema disponível no momento em que decide. Indisponibilidades frequentes levam o usuário a procurar alternativas. No 2º período, a disponibilidade depende sobretudo da organização do código e da atenção à estabilidade durante os testes. | | | |

RNF-008 – Privacidade do usuário

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ID Descrição Status Prioridade
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ ---------------
 RNF-008 O sistema deve coletar apenas as informações necessárias ao funcionamento da plataforma, e o usuário deve controlar quais dados pessoais ficam visíveis a outros usuários. Métricas: (1) no máximo 4 campos obrigatórios no cadastro inicial (nome, e-mail, senha, tipo de conta); (2) o usuário deve conseguir ocultar ou remover qualquer informação opcional do perfil em no máximo 2 cliques; (3) nenhum dado pessoal de contato (telefone, e-mail particular) deve ser exibido a outros usuários sem ação explícita do próprio usuário. Levantado Alta

 Detalhamento: A privacidade sustenta a confiança do usuário. Coletar dados desnecessários ou expor informações pessoais sem consentimento afasta o público-alvo e contradiz os valores do Roomy. O controle do usuário sobre os próprios dados deve guiar as decisões de design, alinhando-se à RNE-007. Esse requisito materializa os princípios da finalidade e da necessidade da LGPD (Lei nº 13.709/2018, art. 6º, I e III).
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

RNF-009 – Acessibilidade básica

 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ID Descrição Status Prioridade
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------ ---------------
 RNF-009 O sistema deve ser utilizável por pessoas com diferentes níveis de familiaridade tecnológica, evitando excesso de jargões e fluxos confusos. Métricas: (1) contraste suficiente entre texto e fundo para leitura confortável; (2) todos os campos de formulário devem conter rótulo (label) visível; (3) nenhuma funcionalidade crítica deve depender exclusivamente de gestos avançados (ex: swipe duplo, pinch) sem alternativa por toque simples. Levantado Média

 Detalhamento: Embora o público-alvo seja jovem, a familiaridade digital varia: um estudante que chega pela primeira vez a uma grande cidade pode ter menos experiência com plataformas de locação. A interface deve atender essa diversidade sem prejudicar quem já tem prática.
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

RNF-010 – Manutenibilidade

| ID | Descrição | Status | Prioridade |
| RNF-010 | O código-fonte deve ser organizado, legível e documentado, de forma que a equipe consiga compreender, manter e expandir o projeto ao longo dos semestres. Métricas: (1) estrutura de pastas documentada no README do repositório; (2) cada arquivo deve conter cabeçalho com descrição de sua responsabilidade; (3) funções com mais de 20 linhas devem ter comentário explicativo. | Levantado | Média |
| | | | |
| | Boas práticas de nomenclatura e organização de pastas devem ser adotadas desde o início. | | |
| Detalhamento: O projeto será desenvolvido de forma incremental por uma equipe de estudantes ao longo de oito semestres. Código desorganizado dificulta retomar o trabalho após pausas, localizar erros e integrar novos membros à equipe. Boas práticas desde o início evitam o acúmulo de problemas nos períodos finais. | | | |

RNF-011 – Escalabilidade futura

 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 ID Descrição Status Prioridade
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------ ---------------
 RNF-011 O sistema deve ser estruturado de forma que permita a adição de novas funcionalidades e o aumento gradual do número de usuários ao longo dos semestres, sem exigir uma reestruturação completa da solução. Métricas: (1) a arquitetura deve ser dividida em no mínimo 2 camadas separadas (ex: frontend e backend); (2) cada funcionalidade deve ser implementada em arquivo(s) de responsabilidade única, sem mistura de lógica de negócio com apresentação. Levantado Baixa

 Detalhamento: A cada período novas funcionalidades serão acrescentadas ao sistema. Uma arquitetura dividida em camadas, com responsabilidades separadas, permite que essas adições ocorram sem reescrever o que já funciona, evitando o acúmulo de dívida técnica nos semestres finais.
 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

