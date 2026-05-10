## Changelog : complements-alimentaires (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du processus de visa des compléments alimentaires, notamment avec l'introduction d'une approbation automatique et d'une interface utilisateur dédiée. Des corrections et améliorations ont également été apportées à l'export des données, à la composition des PDF et à la gestion des images. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Ajout d'une interface utilisateur pour l'approbation automatique du visa des compléments alimentaires. [#2884](https://github.com/betagouv/complements-alimentaires/pull/2884)
- Implémentation de l'approbation automatique du visa en backend. [#2884](https://github.com/betagouv/complements-alimentaires/pull/2884)
- Ajout de l'email de l'entreprise à l'export avancé pour faciliter l'identification. [#2851](https://github.com/betagouv/complements-alimentaires/pull/2851)
- Correction de l'affichage des images. [#2871](https://github.com/betagouv/complements-alimentaires/pull/2871)
- Correction d'un bug lié à l'export des données Open Data. [#2855](https://github.com/betagouv/complements-alimentaires/pull/2855)
- Amélioration de la composition des PDF, notamment avec l'ajout du numéro de page et la correction de l'affichage du symbole "micro" remplacé par un "u". [#2882](https://github.com/betagouv/complements-alimentaires/pull/2882)

### Évolutions techniques
- Refonte de la gestion des paramètres pour l'auto-visa afin d'éviter les conflits.
- Suppression des notebooks au profit de Metabase pour une meilleure gestion des données. [#2872](https://github.com/betagouv/complements-alimentaires/pull/2872)
- Mise à jour de nombreuses dépendances : Django, pypdf, pillow, djangorestframework, charset-normalizer, celery, pytest, vue, postcss, tailwindcss, numpy, click, botocore, tinycss2, sentry-sdk, faker, lxml, github-actions. Ces mises à jour visent à améliorer la sécurité, la performance et la stabilité de l'application.

### Autres changements
- Ajout d'une clé dans le fichier `.env`.
- Correction d'un problème potentiel lié à la valeur nulle de l'attribut `company`.
- Mise à jour de la documentation (README).
- Utilisation d'une balise de template statique pour construire le chemin des images.
- Ajout de fixtures pour faciliter les tests et le développement. [#2843](https://github.com/betagouv/complements-alimentaires/pull/2843)
