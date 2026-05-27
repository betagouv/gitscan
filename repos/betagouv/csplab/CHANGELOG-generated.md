## Changelog : csplab (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions de csplab se concentrent sur l'amélioration de l'ingestion de données (notamment via des webhooks et la gestion des sources), l'ajout de nouvelles fonctionnalités pour les candidats (pages statiques, affichage d'informations sur les offres) et l'amélioration de la qualité du code et des tests. Des efforts ont également été faits pour documenter davantage le projet et faciliter son déploiement.

### Évolutions fonctionnelles
- Ajout de la prise en charge des webhooks TalentSoft pour l'ingestion d'offres d'emploi [#500](https://github.com/betagouv/csplab/issues/500).
- Possibilité d'archiver des offres via des webhooks [#455](https://github.com/betagouv/csplab/issues/455).
- Affichage de l'organisation ou du ministère sur les cartes et dans les détails des offres [#443](https://github.com/betagouv/csplab/issues/443).
- Ajout de pages statiques pour les mentions légales, la politique de confidentialité et l'accessibilité [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226).
- Amélioration de l'affichage des offres d'emploi pour les candidats, notamment avec la possibilité de fermer la fenêtre modale via le navigateur [#444](https://github.com/betagouv/csplab/issues/444).
- Intégration de la catégorie A+ dans le filtre des offres [#482](https://github.com/betagouv/csplab/issues/482).
- Ajout d'une fonctionnalité pour vectoriser les métiers [#551](https://github.com/betagouv/csplab/issues/551).

### Évolutions techniques
- Refactorisation de l'architecture d'ingestion pour une meilleure gestion des sources d'offres [#574](https://github.com/betagouv/csplab/issues/574), [#583](https://github.com/betagouv/csplab/issues/583).
- Amélioration de la gestion des logs dans l'ingestion, avec possibilité de configurer le niveau de log via une variable d'environnement [#594](https://github.com/betagouv/csplab/issues/594).
- Mise en place de tests E2E avec Playwright pour l'interface candidat [#490](https://github.com/betagouv/csplab/issues/490).
- Refactorisation du code pour utiliser des noms de méthodes plus standardisés (get_xxxx) [#568](https://github.com/betagouv/csplab/issues/568).
- Amélioration de la documentation de l'API et des commandes d'ingestion [#472](https://github.com/betagouv/csplab/issues/472), [#480](https://github.com/betagouv/csplab/issues/480).
- Mise à jour des dépendances pour les différents composants (web, ingestion, notebook, ocr) [#570](https://github.com/betagouv/csplab/issues/570), [#571](https://github.com/betagouv/csplab/issues/571), [#495](https://github.com/betagouv/csplab/issues/495), [#497](https://github.com/betagouv/csplab/issues/497).
- Amélioration de la robustesse de la gestion des erreurs dans l'ingestion [#509](https://github.com/betagouv/csplab/issues/509).
- Utilisation de `SettingsConfigDict` pour remplacer la configuration Pydantic dépréciée [#489](https://github.com/betagouv/csplab/issues/489).

### Autres changements
- Ajout de Git hooks pour améliorer la qualité du code [#472](https://github.com/betagouv/csplab/issues/472).
- Mise à jour du fichier CHANGELOG.md pour les versions 0.1.8 et 0.1.9 [#485](https://github.com/betagouv/csplab/issues/485), [#606](https://github.com/betagouv/csplab/issues/606).
- Amélioration de la configuration pour les tests en mode développement [#448](https://github.com/betagouv/csplab/issues/448).
- Nettoyage du code et suppression de configurations inutilisées [#459](https://github.com/betagouv/csplab/issues/459).
- Correction de bugs divers liés à la gestion des caractères spéciaux, des chemins de fichiers et des tests [#505](https://github.com/betagouv/csplab/issues/505), [#511](https://github.com/betagouv/csplab/issues/511), [#529](https://github.com/betagouv/csplab/issues/529), [#546](https://github.com/betagouv/csplab/issues/546).
