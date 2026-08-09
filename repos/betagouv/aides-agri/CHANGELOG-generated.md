## Changelog : aides-agri (30 derniers jours, au 07 août 2026)

### Résumé
Ce mois-ci, la plateforme a renforcé son ouverture de données via l'automatisation des exports vers data.gouv.fr et a enrichi ses outils de gestion interne. La couverture géographique s'est également étendue avec l'intégration de la Normandie, tandis que l'expérience de relecture des aides a été fluidifiée pour les administrateurs.

### Évolutions fonctionnelles
- **Partage de données** : Mise en place d'un export hebdomadaire automatisé vers data.gouv.fr, accompagné de plusieurs améliorations et correctifs de fiabilité ([#620](https://github.com/betagouv/aides-agri/pull/620), [#707](https://github.com/betagouv/aides-agri/pull/707), [#714](https://github.com/betagouv/aides-agri/pull/714), [#716](https://github.com/betagouv/aides-agri/pull/716)).
- **Gestion du back-office** :
    - Amélioration de la visibilité des aides clôturées dans la vue liste ([#715](https://github.com/betagouv/aides-agri/pull/715)).
    - Extension des droits de relecture pour les bureaux valideurs sur les aides déjà publiées ([#700](https://github.com/betagouv/aides-agri/pull/700)).
    - Affichage systématique du lien de partage pour la relecture, même en mode de publication minimal ([#699](https://github.com/betagouv/aides-agri/pull/699)).
- **Contenu et données** :
    - Ajout de la Normandie aux régions couvertes par le catalogue ([#667](https://github.com/betagouv/aides-agri/pull/667)).
    - Mise à disposition des statistiques d'utilisation pour le mois de juillet 2026 ([#697](https://github.com/betagouv/aides-agri/pull/697)).
- **Corrections** : Résolution d'un bug empêchant l'ouverture de certains liens externes ([#696](https://github.com/betagouv/aides-agri/pull/696)).

### Évolutions techniques
- **CI/CD et Infrastructure** : Consolidation des workflows GitHub Actions et optimisation de la chaîne d'intégration continue ([#702](https://github.com/betagouv/aides-agri/pull/702), [#706](https://github.com/betagouv/aides-agri/pull/706)).
- **Gestion des dépendances** : Mise à jour de la gestion des environnements via l'outil `uv` ([#713](https://github.com/betagouv/aides-agri/pull/713)).
- **Tests** : Ajustements et améliorations de la suite de tests automatisés ([#701](https://github.com/betagouv/aides-agri/pull/701)).
