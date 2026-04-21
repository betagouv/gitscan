## Changelog : srdt (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'assistant virtuel SRDT a bénéficié d'améliorations significatives en termes de performance et de fonctionnalités. Un tableau de bord public avec des statistiques d'utilisation a été ajouté, permettant un suivi plus précis de l'activité. Des corrections ont été apportées pour améliorer la qualité des réponses et la gestion des liens vers les conventions collectives. L'utilisation de ChatGPT a été rétablie pour améliorer les temps de réponse.

### Évolutions fonctionnelles
- Ajout d'un badge de convention collective sur les messages de l'assistant dans l'interface de chat. [#344](https://github.com/SocialGouv/srdt/issues/344)
- Mise en place d'une page publique de statistiques avec un tableau de bord Metabase intégré, offrant une vue d'ensemble de l'utilisation de l'assistant. [#327](https://github.com/SocialGouv/srdt/issues/327)
- Amélioration de la gestion des liens directs vers les conventions collectives. [#319](https://github.com/SocialGouv/srdt/issues/319)
- Retour à l'utilisation de ChatGPT pour améliorer les temps de réponse du modèle de langage. [#341](https://github.com/SocialGouv/srdt/issues/341)

### Évolutions techniques
- Ajout d'une colonne `followup_count` dans la base de données pour le suivi des interactions avec Metabase. [#326](https://github.com/SocialGouv/srdt/issues/326)
- Possibilité d'effectuer des appels de débogage sur l'API `/api/generate` en utilisant un token bearer. [#346](https://github.com/SocialGouv/srdt/issues/346)
- Mise à jour du prompt utilisé par le modèle de langage pour améliorer la qualité des réponses. [#341](https://github.com/SocialGouv/srdt/issues/341) et [#316](https://github.com/SocialGouv/srdt/issues/316)

### Autres changements
- Correction du placeholder de suivi pour une meilleure expérience utilisateur. [#347](https://github.com/SocialGouv/srdt/issues/347)
- Correction de la reconstruction des URLs des articles. [#316](https://github.com/SocialGouv/srdt/issues/316)
