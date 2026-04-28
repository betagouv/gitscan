## Changelog : srdt (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'assistant virtuel SRDT a bénéficié d'améliorations significatives en termes de fonctionnalités et de performances. Une page de statistiques publiques a été ajoutée, permettant un suivi de l'utilisation. Des corrections ont été apportées pour améliorer la fiabilité et la réactivité du modèle de langage, ainsi que l'affichage des informations sur les conventions collectives.

### Évolutions fonctionnelles
- Ajout d'un badge de convention collective sur les messages de l'assistant pour une meilleure identification du contexte juridique [#344](https://github.com/SocialGouv/srdt/issues/344).
- Mise en place d'une page de statistiques publiques avec un tableau de bord Metabase intégré, offrant une vue d'ensemble de l'utilisation du service [#327](https://github.com/SocialGouv/srdt/issues/327).
- Amélioration de l'affichage des liens directs vers les conventions collectives [#319](https://github.com/SocialGouv/srdt/issues/319).
- Possibilité d'appeler l'API `/api/generate` en mode debug avec un token bearer pour faciliter le diagnostic et le développement [#346](https://github.com/SocialGouv/srdt/issues/346).
- Amélioration du placeholder de suivi pour une meilleure expérience utilisateur [#347](https://github.com/SocialGouv/srdt/issues/347).

### Évolutions techniques
- Retour à l'utilisation de ChatGPT pour améliorer les temps de réponse du modèle de langage [#341](https://github.com/SocialGouv/srdt/issues/341).
- Restauration du modèle Mistral LLM, puis retour à ChatGPT en raison des performances [#341](https://github.com/SocialGouv/srdt/issues/341).
- Ajout de la colonne `followup_count` dans la base de données pour le suivi par Metabase [#326](https://github.com/SocialGouv/srdt/issues/326).
- Mise à jour des prompts utilisés par le modèle de langage (CC_2 et autres) pour améliorer la qualité des réponses.

### Autres changements
-  Aucun changement significatif à signaler dans cette catégorie.
