## Changelog : la_taupe (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci, la_taupe a franchi une étape importante avec l'intégration d'un nouveau moteur d'OCR plus performant et l'ajout de fonctionnalités de traitement par lots (batch) via l'interface en ligne de commande. L'extraction des informations critiques des RIB (titulaire, BIC, IBAN) est devenue plus robuste et précise, notamment grâce à une meilleure gestion des mises en page complexes.

### Évolutions fonctionnelles
- **Traitement par lots (Batch) :** L'interface en ligne de commande (CLI) permet désormais d'analyser des fichiers ou des répertoires entiers de RIB en une seule commande, avec une option `--type` pour spécifier l'analyse. [#64](https://github.com/demarche-numerique/la_taupe/pull/64)
- **Amélioration de l'extraction des RIB :**
    - Détection plus fiable du BIC, y compris pour les formats où une lettre est imprimée par cellule. [#62](https://github.com/demarche-numerique/la_taupe/pull/62)
    - Validation automatique du BIC par rapport à la banque associée à l'IBAN.
    - Meilleure identification du titulaire du compte (nom, adresse, ville) grâce à un ancrage plus robuste des blocs de texte. [#63](https://github.com/demarche-numerique/la_taupe/pull/63)
- **Gestion des documents :** Ajout d'un indicateur pour signaler les documents ne contenant aucune donnée exploitable.

### Évolutions techniques
- **Nouveau moteur OCR :** Passage par défaut au moteur PP-OCR v6 tiny (via ONNX Runtime), offrant une meilleure efficacité pour l'extraction de texte. [#60](https://github.com/demarche-numerique/la_taupe/pull/60)
- **Banc de mesure et performance :** 
    - Mise en place d'un outil de benchmarking et d'un corpus synthétique pour mesurer précisément la précision et la latence du système. [#59](https://github.com/demarche-numerique/la_taupe/pull/59)
    - Optimisations diverses pour réduire la latence de traitement. [#58](https://github.com/demarche-numerique/la_taupe/pull/58)
- **Robustesse de l'OCR et de la mise en page :**
    - Amélioration de la gestion de la rotation des pages et de l'ancrage des éléments clés (IBAN, code postal).
    - Correction de la détection des blocs de texte pour mieux gérer les différents layouts de RIB rencontrés sur le terrain.

### Autres changements
- **Documentation :** Ajout de sections détaillant les méthodologies de mesure et les résultats des expérimentations (notamment sur les tests de reconnaissance d'entités nommées - NER). [#61](https://github.com/demarche-numerique/la_taupe/pull/61)
- **Données :** Mise à jour du registre de la Banque Centrale Européenne (ECB) intégré au projet.
- **Qualité de code :** Intégration de l'outil Clippy pour assurer la conformité et la propreté du code Rust sur l'ensemble des cibles.
