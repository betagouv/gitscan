## Changelog : mon-aide-cyber (30 derniers jours, au 16 avril 2026)

### Résumé
Ce changelog présente les récentes améliorations apportées à MonAideCyber. Les modifications incluent des corrections de bugs, notamment concernant le calcul du cooldown et la gestion des encarts d'homologation, ainsi qu'une gestion améliorée des erreurs renvoyées par l'API Géo. Des mises à jour de dépendances et de composants UI ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Correction du calcul du nombre de jours pour le cooldown dans le module SOIN.
- Correction de l'affichage des encarts d'homologation dans le module SOIN.
- Amélioration de la gestion des erreurs retournées par l'API Géo lors de l'appel EPCI, évitant ainsi des dysfonctionnements. [#issue-potentielle]

### Évolutions techniques
- Mise à jour de la version du UI Kit vers la v1.28.4.
- Suppression d'un UI Kit non utilisé pour alléger le code et simplifier la maintenance.
- Mise à jour de certaines dépendances pour améliorer la sécurité et la stabilité de l'application.

### Autres changements
- Mise à jour des tampons d'homologation MAC.
- Mise à jour de la dépendance `yaml` vers la version 2.8.3.
- Mise à jour de la dépendance `vite` vers la version 7.3.2.
- Mise à jour de la dépendance `happy-dom` vers la version 20.8.9.
