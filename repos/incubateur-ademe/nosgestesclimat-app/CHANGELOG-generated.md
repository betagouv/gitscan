## Changelog : nosgestesclimat-app (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur l'amélioration de la découverte des actions climatiques pour les utilisateurs et une optimisation majeure de l'infrastructure. L'application est devenue plus performante grâce à de nouveaux mécanismes de mise en cache et de rendu, tout en bénéficiant d'outils de suivi (observabilité) plus robustes pour garantir une meilleure stabilité.

### Évolutions fonctionnelles
- **Amélioration de la découverte des actions** : Mise en place d'un catalogue d'actions public [#2003], ajout de descriptions courtes pour les actions [#2012] et expérimentation de nouveaux designs via des tests A/B sur les cartes et la mise en page des actions à fort impact [#2006, #1997].
- **Optimisation du parcours utilisateur** : Introduction de suggestions d'actions croisées (cross-sell) [#2010], amélioration des messages d'avertissement [#2004] et correction de la navigation pour conserver les paramètres de recherche lors du passage au tutoriel [#2027].
- **Corrections de bugs et d'interface** : Résolution de problèmes de connexion liés aux sessions [#2047], correction de textes et de coquilles (ex: "SECONDS" en "SECONDES") [#2060, #2029], et correction de comportements erronés dans les simulations (réinitialisation dans les groupes d'amis [#1999] et masquage d'actions dans le catalogue personnalisé [#2002]).

### Évolutions techniques
- **Infrastructure et Proxy** : Refonte de la configuration Nginx pour améliorer la résilience (DNS, timeouts [#1966, #2074]) et optimiser la gestion des fichiers statiques et du contenu via un proxy (S3/CMS [#1950, #2081]) et une mise en cache étendue des pages publiques [#1953, #2076].
- **Observabilité et Monitoring** : Intégration poussée de PostHog pour le suivi des erreurs et des logs via OpenTelemetry [#2051, #2067], mise en place d'un reverse proxy pour PostHog [#2063, #2048] et ajout de statistiques Matomo [#2057].
- **Performance et Scalabilité** : Optimisation du rendu de la page d'accueil via le Partial Prerendering (PPR) [#2041], amélioration de l'efficacité des requêtes de simulation en base de données [#2049, #2036] et réduction des allers-retours serveur lors des changements de paramètres [#2035].
- **Stabilité et Qualité logicielle** : Renforcement des tests de bout en bout (E2E) avec Playwright [#2077, #1993], augmentation de la mémoire des workers pour éviter les plantages [#2046] et sécurisation de l'intégrité des données via des contraintes de clés étrangères et de sessions [#2016, #1973].
- **Refactoring** : Nettoyage du code avec la suppression de logiques et de tables obsolètes (SimulationState, extendedSituation) [#2031, #2032] et refactorisation du calcul des statistiques de campagne [#2028].

### Autres changements
- Ajout d'un script pour la génération d'URLs FGP [#2058].
