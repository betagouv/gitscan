## Changelog : csplab (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion de données, notamment avec l'ajout de la prise en charge des webhooks TalentSoft et l'archivage des offres. Des améliorations significatives ont également été apportées à l'interface candidat, avec l'ajout de pages légales, des tests E2E et des améliorations de l'expérience utilisateur. Enfin, des optimisations techniques ont été réalisées pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout d'un endpoint API pour lister les offres [#440](https://github.com/betagouv/csplab/issues/440).
- Intégration d'un endpoint webhook pour l'import de données TalentSoft [#500](https://github.com/betagouv/csplab/issues/500).
- Ajout de pages statiques pour les mentions légales, la politique de confidentialité et l'accessibilité [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#227](https://github.com/betagouv/csplab/issues/227).
- Amélioration de l'affichage des organisations/ministères dans les cartes et les tiroirs d'opportunités [#443](https://github.com/betagouv/csplab/issues/443).
- Amélioration du CV MVP : styles et contenu mis à jour [#441](https://github.com/betagouv/csplab/issues/441).
- Possibilité de fermer le tiroir modal de CV en utilisant la navigation du navigateur [#444](https://github.com/betagouv/csplab/issues/444).
- Le filtre de catégorie des candidats inclut désormais A+ [#482](https://github.com/betagouv/csplab/issues/482).
- Possibilité d'archiver des offres [#455](https://github.com/betagouv/csplab/issues/455).
- Les documents ayant échoué lors de l'ingestion ne restent plus en attente et ne sont pas retraités [#452](https://github.com/betagouv/csplab/issues/452).
- Mise à jour des filtres actifs dans l'interface utilisateur lors du chargement de la page [#380](https://github.com/betagouv/csplab/issues/380).

### Évolutions techniques
- Refonte de l'architecture d'ingestion avec la création d'une nouvelle application dédiée [#493](https://github.com/betagouv/csplab/issues/493).
- Suppression de l'utilisation de `pgvector` et du modèle `VectorizedDocumentModel` [#385](https://github.com/betagouv/csplab/issues/385).
- Mise en place d'une file d'attente asynchrone pour le traitement des CV et des tâches d'indexation [#376](https://github.com/betagouv/csplab/issues/376).
- Amélioration de la documentation de l'API [#396](https://github.com/betagouv/csplab/issues/396) et des commandes de chargement [#481](https://github.com/betagouv/csplab/issues/481).
- Refactorisation des tests, notamment avec l'ajout de tests E2E avec Playwright [#490](https://github.com/betagouv/csplab/issues/490) et la suppression des tests de vue remplacés par des tests E2E [#462](https://github.com/betagouv/csplab/issues/462).
- Amélioration de la configuration et de l'environnement de développement (gestion des tâches périodiques, override des ports, etc.).
- Mise à jour des dépendances (pypdf, notebook, ocr, tycho) [#382](https://github.com/betagouv/csplab/issues/382), [#383](https://github.com/betagouv/csplab/issues/383), [#397](https://github.com/betagouv/csplab/issues/397), [#401](https://github.com/betagouv/csplab/issues/401), [#402](https://github.com/betagouv/csplab/issues/402), [#495](https://github.com/betagouv/csplab/issues/495), [#496](https://github.com/betagouv/csplab/issues/496), [#497](https://github.com/betagouv/csplab/issues/497).

### Autres changements
- Ajout de tests de couverture de code [#498](https://github.com/betagouv/csplab/issues/498).
- Mise à jour du CHANGELOG pour les versions 0.1.7 et 0.1.8 [#375](https://github.com/betagouv/csplab/issues/375), [#418](https://github.com/betagouv/csplab/issues/418).
- Amélioration de la journalisation (logging) avec l'utilisation d'interpolation de chaînes paresseuses [#412](https://github.com/betagouv/csplab/issues/412).
- Correction de bugs mineurs (gestion des caractères non encodés dans les signatures, gestion des dates d'expiration, isolation des documents bruts en cas d'erreur d'ingestion).
- Amélioration de la documentation pour l'installation des hooks Git [#472](https://github.com/betagouv/csplab/issues/472) et des dépendances locales pour l'OCR [#453](https://github.com/betagouv/csplab/issues/453).
- Renommage des méthodes `find_by_xx` en `get_by_xx` pour plus de cohérence [#458](https://github.com/betagouv/csplab/issues/458).
- Suppression de code inutilisé et refactorisation de certains composants.
