## Changelog : csv-detective (30 derniers jours, au 18 mars 2026)

### Résumé
Cette version apporte des améliorations significatives à la détection des formats de données, notamment pour les codes INSEE, les dates et les nombres. Des corrections ont également été apportées pour améliorer la précision de l'analyse des fichiers, en particulier concernant les valeurs manquantes et les erreurs de conversion. Enfin, la gestion des encodages a été revue.

### Évolutions fonctionnelles
- Ajout du format `code_epci` pour la détection des codes d'établissements publics de coopération intercommunale. [#214](https://github.com/datagouv/csv-detective/pull/214)
- Possibilité de définir des proportions personnalisées pour les formats détectés. [#213](https://github.com/datagouv/csv-detective/pull/213)
- Amélioration de la détection des nombres en notation scientifique, y compris pour les nombres négatifs. [#229](https://github.com/datagouv/csv-detective/pull/229)
- Correction de la détection des dates dans certains formats (RFC822 et dates avec fuseau horaire). [#226](https://github.com/datagouv/csv-detective/pull/226), [#227](https://github.com/datagouv/csv-detective/pull/227)
- Correction du nom du format `code_commune_insee` qui a été renommé `code_commune` pour une meilleure cohérence. [#215](https://github.com/datagouv/csv-detective/pull/215)

### Évolutions techniques
- Changement de la librairie de détection d'encodage pour une meilleure performance et précision. [#218](https://github.com/datagouv/csv-detective/pull/218)
- Correction du calcul du nombre de valeurs manquantes dans les fichiers analysés par blocs (chunked).
- Suppression de code mort dans le module `siret.py`. [#228](https://github.com/datagouv/csv-detective/pull/228)
- Amélioration de la gestion des `NaN` et `inf` lors de la création du profil des données. [#235](https://github.com/datagouv/csv-detective/pull/235)
- Correction d'une erreur qui empêchait la publication automatique lors des commits sur la branche principale. [#216](https://github.com/datagouv/csv-detective/pull/216)

### Autres changements
- Ajout de tests pour vérifier que tous les formats ont une description (label). [#231](https://github.com/datagouv/csv-detective/pull/231)
- Correction de typos et amélioration de la lisibilité du code.
- Correction de problèmes mineurs dans les exemples de sortie du schéma. [#224](https://github.com/datagouv/csv-detective/pull/224)
- Correction du nom de fichier exporté contenant le nom de la feuille. [#230](https://github.com/datagouv/csv-detective/pull/230)
- Correction de la gestion des chaînes vides dans la détection des pourcentages et des montants monétaires. [#222](https://github.com/datagouv/csv-detective/pull/222)
- Correction d'une erreur qui empêchait la validation si le format détecté était une chaîne de caractères. [#232](https://github.com/datagouv/csv-detective/pull/232)
- Amélioration de la gestion des entiers trop longs, qui n'étaient pas correctement détectés comme des entiers ou des flottants. [#233](https://github.com/datagouv/csv-detective/pull/233)
