## Changelog : espace-membre-next (30 derniers jours, au 05/11/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'accueil des nouveaux membres (onboarding) et la sécurisation des accès via ProConnect et l'authentification multi-facteurs (MFA). Plusieurs correctifs ont également été apportés pour fluidifier la gestion des emails et stabiliser les outils de support et de réservation.

### Évolutions fonctionnelles
- **Accompagnement et Onboarding** : Mise en place d'une checklist dédiée aux nouveaux intrapreneurs [#1580], d'un module d'e-learning sur la sélection des prestataires [#1598] et correction du parcours d'inscription pour les anciens profils [#1608].
- **Authentification et Sécurité** : Nouveau flux de connexion ProConnect incluant le MFA et les liens magiques [#1569], ainsi qu'une meilleure gestion des erreurs et des motifs de refus lors de la connexion [#1603, #1597, #1596].
- **Outils et Services** : Remplacement de l'outil Crisp par le widget Messages pour le support [#1611] et rétablissement de la fonctionnalité de réservation de salles de réunion [#1606].
- **Gestion métier** : Amélioration de la gestion des adresses Dimail (synchronisation et réactivation) [#1588, #1628], correction des droits d'édition des fiches produits pour les membres en mission [#1626] et résolution de problèmes liés aux adresses de connexion [#1627].

### Évolutions techniques
- **API** : Renforcement de la sécurité de l'API v1 avec des clés à portée restreinte [#1518] et ajout de données de communication dans les réponses membres [#1615].
- **Infrastructure et Déploiement** : Refonte de la gestion des tâches planifiées (cron) [#1590], automatisation des exports vers beta.gouv.fr [#1602] et correction du processus de migration lors des déploiements [#1595].
- **Maintenance et Sécurité** : Mise à jour majeure vers React 19 [#1600], correction de vulnérabilités critiques (Zod 4 [#1619], npm audit [#1616]) et resynchronisation des tests automatisés [#1594].
