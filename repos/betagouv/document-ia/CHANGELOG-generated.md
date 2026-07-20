## Changelog : document-ia (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, le projet document-ia a connu une évolution significative avec l'introduction de la version 1.0.7 et le développement de la version 2 des workflows. Des améliorations ont été apportées à l'OCR Mistral, à la gestion des données fiscales (taxe foncière) et à la console d'administration. La sécurité a également été renforcée avec la correction de vulnérabilités.

### Évolutions fonctionnelles
- Ajout d'une page dans la console pour exécuter les workflows V2 [#71](https://github.com/betagouv/document-ia/issues/71).
- Amélioration de la gestion des identités pour la taxe foncière, permettant désormais de gérer plusieurs identités par document [#74](https://github.com/betagouv/document-ia/issues/74) et [#75](https://github.com/betagouv/document-ia/issues/75).
- Création d'une version 2 de la page "ground truth" pour l'annotation de données [#72](https://github.com/betagouv/document-ia/issues/72).
- Correction d'un bug dans le worker qui empêchait le chargement correct des JSON 2Ddoc contenant des dates [#84](https://github.com/betagouv/document-ia/issues/84).
- Correction d'un problème avec l'OCR Mistral qui ne séparait pas correctement le contenu des tableaux [#85](https://github.com/betagouv/document-ia/issues/85) et [#83](https://github.com/betagouv/document-ia/issues/83).
- Ajout d'une tâche de réplication pour déplacer les données anonymisées [#86](https://github.com/betagouv/document-ia/issues/86).

### Évolutions techniques
- Mise en place d'un auto-scaler pour le worker sur Scalingo [#80](https://github.com/betagouv/document-ia/issues/80).
- Correction d'une vulnérabilité (CVE) dans la librairie Starlette [#72](https://github.com/betagouv/document-ia/issues/72).
- Refonte du fichier `README.md` et du template de Pull Request [#82](https://github.com/betagouv/document-ia/issues/82).
- Mise à jour de la documentation et du guide de contribution [#78](https://github.com/betagouv/document-ia/issues/78).
- Amélioration de la structure des workflows [#69](https://github.com/betagouv/document-ia/issues/69).

### Autres changements
- Publication de la version 1.0.7 [#81](https://github.com/betagouv/document-ia/issues/81).
- Mise à jour de la documentation et des instructions de test pour le worker [#79](https://github.com/betagouv/document-ia/issues/79).
