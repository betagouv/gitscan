## Changelog : benefriches (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois a été marqué par deux axes majeurs : l'amélioration de la précision des calculs d'impact (score de développement) et le déploiement d'un système complet de communication automatisée par email. L'expérience utilisateur a également été fluidifiée grâce à un nouvel onboarding et une simplification des formulaires de saisie.

### Évolutions fonctionnelles
- **Calculs et Scores** : Amélioration de la précision du "score de développement", notamment pour les projets photovoltaïques et les calculs liés à la décontamination des sols.
- **Système d'emails** : Mise en place d'un cycle de vie complet d'emails automatisés (bienvenue, rappels quotidiens, résumés d'impacts à la création de projet) incluant la gestion des désinscriptions et un design conforme au DSFR.
- **Expérience Utilisateur (UX)** : 
    - Refonte du parcours d'onboarding avec un nouveau flux en 3 étapes.
    - Simplification des formulaires de décontamination (regroupés en une seule étape).
    - Amélioration de la navigation via une barre latérale plus intuitive et un assistant de mise à jour (wizard) harmonisé.
    - Accès facilité au chat de support, même pour les visiteurs non connectés.
- **Données de référence** : Mise à jour des bases de données de villes avec les dernières statistiques de l'ANCT, les zonages (ABC/ALDO) et les données foncières DVF 2025.

### Évolutions techniques
- **Infrastructure** : Migration vers NestJS 12.
- **Architecture** : Refactorisation importante pour centraliser les calculs de score, les indicateurs d'impact et les formatteurs de données dans un module partagé (`shared`), améliorant la cohérence entre l'API et le Web.
- **Fiabilité** : Ajout d'un mécanisme de relance automatique (*retry sweeper*) pour garantir la délivrance des emails.
- **Sécurité et API** : Amélioration de l'identification des auteurs lors de la création de projets et de sites en utilisant les jetons d'accès (access tokens).

### Autres changements
- **Documentation** : Restructuration de la documentation (séparation de la doc "impacts" sur une page dédiée) et ajout de nouveaux guides de contrôle qualité (QA).
- **Maintenance** : Nettoyage de la configuration des agents de développement et corrections typographiques diverses.
