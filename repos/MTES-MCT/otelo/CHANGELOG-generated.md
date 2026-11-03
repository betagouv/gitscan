## Changelog : otelo (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci a été marqué par une refonte majeure de l'expérience utilisateur, notamment avec un nouveau parcours guidé (wizard) et l'introduction d'un mode tutoriel pour faciliter la prise en main de l'outil. L'application s'enrichit également de nouveaux outils de visualisation (pyramide des âges) et de fonctionnalités de planification, tout en renforçant significativement la sécurité des accès et la robustesse de l'infrastructure.

### Évolutions fonctionnelles
- **Refonte de l'expérience utilisateur** : Nouveau parcours guidé (wizard) pour accompagner l'utilisateur de la configuration des paramètres jusqu'à l'obtention des résultats. [#73](https://github.com/MTES-MCT/otelo/pull/73), [#74](https://github.com/MTES-MCT/otelo/pull/74)
- **Aide et accompagnement** : Mise en place d'un mode tutoriel interactif (didacticiel) couvrant les six étapes de création d'une simulation.
- **Nouvelles fonctionnalités d'analyse** : Ajout d'une pyramide des âges, d'un volet de planification territoriale et intégration de la fonctionnalité Docurba.
- **Amélioration des données et exports** : Optimisation des calculs (logements vacants, millésimes démographiques), amélioration des graphiques et fiabilisation des exports (Excel, CSV, PowerPoint).
- **Sécurité renforcée** : Introduction de l'authentification à deux facteurs (2FA).
- **Administration et suivi** : Refonte de l'interface d'administration et mise en place d'un suivi d'usage via Matomo et base de données.

### Évolutions techniques
- **Cartographie** : Optimisation de MapLibre, notamment sur la gestion des workers et la correction de l'affichage des bassins EPCI dans les territoires d'étude. [#76](https://github.com/MTES-MCT/otelo/pull/76)
- **Sécurité système** : Renforcement de la sécurité via l'implémentation de headers CSP, de la limitation de débit (rate limiting) et de la sécurisation des routes de récupération de mot de passe.
- **Infrastructure et CI/CD** : Passage à Node.js 24 (LTS), optimisation de la taille des images Docker pour l'API et ajustements du pipeline de build.
- **Architecture** : Refactorisation du registre des étapes du parcours de scénario pour une meilleure gestion interne.

### Autres changements
- Mise à jour de la documentation du projet (README).
