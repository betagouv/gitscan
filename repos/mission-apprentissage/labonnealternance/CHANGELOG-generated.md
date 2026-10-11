## Changelog : labonnealternance (30 derniers jours, au 09 octobre 2026)

### Résumé
Ce mois a été marqué par un effort majeur de mise en conformité pour l'accessibilité (RGAA 11), le lancement du module "Offres 100% libres" et une refonte technique du moteur de recherche pour améliorer la précision des résultats. L'expérience utilisateur a également été enrichie par l'intégration de nouveaux flux de données (Hellowork, APEC, LinkedIn) et une meilleure gestion de la conservation des données (CV).

### Évolutions fonctionnelles
- **Accessibilité (RGAA 11) :** Mise en conformité massive de l'interface, incluant les filtres de recherche [#5631](https://github.com/mission-apprentissage/labonnealternance/issues/5631), les formulaires de connexion/création de compte [#5617](https://github.com/mission-apprentissage/labonnealternance/issues/5617), les réponses CFA [#5621](https://github.com/mission-apprentissage/labonnealternance/issues/5621), les formulaires de candidature et de rendez-vous [#5600](https://github.com/mission-apprentissage/labonnealternance/issues/5600), ainsi que les outils d'administration [#5622](https://github.com/mission-apprentissage/labonnealternance/issues/5622).
- **Nouveautés et Contenu :** 
    - Lancement du MVP des "Offres 100% libres" avec modération par IA [#5078](https://github.com/mission-apprentissage/labonnealternance/issues/5078).
    - Création de pages dédiées aux diplômes (niveaux bac+2 et inférieurs) pour faciliter la navigation [#5605](https://github.com/mission-apprentissage/labonnealternance/issues/5605).
    - Intégration de nouveaux flux d'offres via Hellowork, APEC [#5550](https://github.com/mission-apprentissage/labonnealternance/issues/5550) et LinkedIn [#5482](https://github.com/mission-apprentissage/labonnealternance/issues/5482).
- **Recherche et Navigation :** 
    - Amélioration de la recherche par département et région [#5461](https://github.com/mission-apprentissage/labonnealternance/issues/5461).
    - Mise à jour de la cartographie des CFA [#5660](https://github.com/mission-apprentissage/labonnealternance/issues/5660).
    - Optimisation du SEO avec des méta-descriptions dynamiques sur les fiches offres [#5613](https://github.com/mission-apprentissage/labonnealternance/issues/5613).
- **Expérience Utilisateur :** 
    - Mise en place de la conservation des CV pendant un an avec purge automatique [#5518](https://github.com/mission-apprentissage/labonnealternance/issues/5518).
    - Affichage explicite des offres indisponibles sur les fiches détails [#5654](https://github.com/mission-apprentissage/labonnealternance/issues/5654).
    - Corrections diverses sur les formulaires (SIRET, candidatures, création de compte) pour éviter les pertes de saisie ou les erreurs d'affichage.

### Évolutions techniques
- **Moteur de recherche :** Refonte de l'architecture d'indexation avec le passage à une gestion par collection dédiée pour améliorer les performances et la fiabilité des suggestions [#5527](https://github.com/mission-apprentissage/labonnealternance/issues/5527).
- **API & Backend :** 
    - Évolution de l'API v3 pour exposer de nouveaux champs (début de contrat, questions recruteurs) [#5471](https://github.com/mission-apprentissage/labonnealternance/issues/5471).
    - Création d'un endpoint de traitement par lots (batch) pour les partenaires [#5564](https://github.com/mission-apprentissage/labonnealternance/issues/5564).
    - Consolidation de la configuration Brevo sur un compte unique [#5650](https://github.com/mission-apprentissage/labonnealternance/issues/5650).
- **Qualité et CI/CD :** 
    - Automatisation du déclenchement de CodeQL lors des revues de code [#5568](https://github.com/mission-apprentissage/labonnealternance/issues/5568).
    - Mise en place de notifications après les déploiements de preview réussis [#5658](https://github.com/mission-apprentissage/labonnealternance/issues/5658).

### Autres changements
- **Maintenance :** Mise à jour des listes de blocage (blacklist) pour certains CFA [#5523](https://github.com/mission-apprentissage/labonnealternance/issues/5523).
- **Documentation :** Mise à jour des instructions pour les outils d'assistance (Claude/Copilot) et de la convention de nommage des Pull Requests [#5520](https://github.com/mission-apprentissage/labonnealternance/issues/5520).
- **Nettoyage :** Suppression de templates inutilisés [#5644](https://github.com/mission-apprentissage/labonnealternance/issues/5644) et de commentaires obsolètes.
