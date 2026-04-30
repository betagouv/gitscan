## Changelog : srdt (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, l'assistant virtuel SRDT a bénéficié d'améliorations significatives en termes de performance et de fonctionnalités. Des ajustements ont été apportés au modèle de langage utilisé pour optimiser les temps de réponse, et de nouvelles fonctionnalités ont été ajoutées pour améliorer l'expérience utilisateur, notamment un badge d'identification des conventions collectives et une page de statistiques publiques.

### Évolutions fonctionnelles
- Ajout d'un badge indiquant la convention collective sur les messages de l'assistant virtuel ([#344](https://github.com/SocialGouv/srdt/issues/344)).
- Mise en place d'une page de statistiques publiques avec un tableau de bord Metabase intégré ([#327](https://github.com/SocialGouv/srdt/issues/327)).
- Amélioration de l'affichage du placeholder de suivi dans les conversations ([#347](https://github.com/SocialGouv/srdt/issues/347)).
- Possibilité d'appeler l'API `/api/generate` en mode debug avec un token bearer ([#346](https://github.com/SocialGouv/srdt/issues/346)).
- Correction pour conserver les liens directs vers les conventions collectives [#319](https://github.com/SocialGouv/srdt/issues/319).

### Évolutions techniques
- Retour temporaire à ChatGPT pour améliorer les temps de réponse du modèle de langage ([#341](https://github.com/SocialGouv/srdt/issues/341)).
- Restauration de l'utilisation du modèle Mistral LLM après correction des problèmes de performance.
- Mise à jour des prompts utilisés par le modèle de langage (CC_2 et autres).

### Autres changements
- Correction de bugs divers et améliorations mineures.
- Mises à jour de la version du projet (1.38.0 à 1.39.5).
