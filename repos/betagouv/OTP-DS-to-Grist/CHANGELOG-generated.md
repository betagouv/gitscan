## Changelog : OTP-DS-to-Grist (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'outil de synchronisation entre Démarches Simplifiées et Grist au cours des 30 derniers jours. Les changements incluent des corrections de bugs, des améliorations de l'interface utilisateur (notamment concernant les logs et le menu), et des optimisations techniques pour une meilleure performance et stabilité. Une nouvelle version (0.6.0) a été publiée.

### Évolutions fonctionnelles
- Ajout d'un bouton pour copier les logs de synchronisation (#171)
- Amélioration de l'interface du formulaire de configuration, notamment avec la correction du volet des logs et la suppression d'un bandeau redondant (#187)
- Correction d'un bug empêchant la synchronisation automatique sans clé Grist (#202)
- Suppression du bouton de menu mobile et refonte du menu principal (#183)
- Ajout d'un lien vers le changelog dans la documentation (#179)

### Évolutions techniques
- Optimisation générale de l'application (#164)
- Mise à jour de plusieurs dépendances :
    - SQLAlchemy (2.0.45 -> 2.0.46)
    - poethepoet (0.38.0 -> 0.40.0)
    - python-socketio (5.16.0)
    - apscheduler (3.11.2)
    - commitizen (4.12.1)
    - baseline-browser-mapping (2.9.18)

### Autres changements
- Nettoyage et amélioration de la documentation du CHANGELOG (#188)
- Amélioration de l'environnement de développement avec une meilleure configuration VS Code (#203)
- Publication de la version 0.6.0 (#185)
