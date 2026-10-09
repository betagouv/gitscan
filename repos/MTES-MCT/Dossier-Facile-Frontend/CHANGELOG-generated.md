## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 07/10/2026)

### Résumé
Les récentes évolutions se concentrent sur l'enrichissement des capacités d'analyse de documents et l'amélioration de l'expérience utilisateur, notamment via une refonte visuelle de la gestion des erreurs. Le projet gagne également en robustesse grâce à une meilleure automatisation des déploiements et une documentation de développement simplifiée pour les contributeurs.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités**
  - Ajout de l'analyse de documents professionnels et de la gestion des erreurs PNDS [#2035](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2035).
  - Possibilité de partager les dossiers en attente de traitement (TO_PROCESS) [#2046](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2046).
  - Mise en place du quota MVP [#2038](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2038).
- **Améliorations de l'interface et de l'expérience utilisateur**
  - Refonte complète du design pour la gestion des erreurs PNDS [#2042](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2042).
  - Ajout d'une fenêtre de confirmation lors de l'annulation d'une demande de validation [#2052](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2052).
  - Amélioration des appels à l'action (callouts) et des boutons de validation [#2048](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2048), [#2053](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2053).
  - Ajustement des textes de la bannière d'adhésion et suppression de la bannière ZIP [#2051](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2051).
  - Amélioration de l'accessibilité via la correction des contrastes [#2041](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2041).
- **Corrections**
  - Correction des libellés concernant la situation déclarative fiscale [#2044](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2044) et les erreurs PNDS [#2043](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2043).

### Évolutions techniques
- **Déploiement et CI/CD**
  - Automatisation du déploiement en environnement de préproduction via GitHub Actions [#2058](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2058).
- **Refactoring et Tests**
  - Refonte du module d'affichage de la progression de l'analyse [#2047](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2047).
  - Amélioration de la stabilité des tests de bout en bout (E2E), notamment sur la gestion de l'attente lors de l'analyse de documents [#2037](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2037).

### Autres changements
- **Documentation**
  - Simplification des instructions pour les agents dans le README [#2055](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2055).
  - Ajout de scripts et de documentation pour faciliter le lancement de l'application en local [#2049](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2049).
- **Configuration**
  - Ajout de la configuration `extensions.json` pour l'extension Vue [#2056](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2056).
  - Mise à jour des exemples d'environnement pour l'utilisation locale de FranceConnect [#2050](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2050).
