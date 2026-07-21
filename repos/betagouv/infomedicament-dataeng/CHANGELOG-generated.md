## Changelog : infomedicament-dataeng (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation et le traitement des données des médicaments, notamment en ajoutant la prise en charge des documents PDF centralisés de l'EMA (Agence Européenne des Médicaments) et en optimisant les performances d'importation des données. De nouvelles fonctionnalités ont également été ajoutées pour faciliter l'importation de datapackages.

### Évolutions fonctionnelles
- Ajout d'une commande CLI `import-datapackage` pour faciliter l'importation de datapackages. [#1234](https://github.com/betagouv/infomedicament-dataeng/issues/1234)
- Intégration de la table `specialite_titulaire` lors de l'importation de datapackages.
- Ajout d'une nouvelle source de données `url_has`.
- Extraction et rendu des images présentes dans les notices d'EMA.

### Évolutions techniques
- Amélioration du traitement des PDF centralisés de l'EMA :
    - Gestion de la limitation de débit (rate-limiting) de l'EMA lors de la récupération des PDF.
    - Rendu des tableaux et parsing par lots (resumable, batched parse).
    - Parsing des PDF centralisés de l'EMA en listes de nodes Notice/RCP.
- Optimisation des performances d'importation des données en utilisant la commande `COPY` au lieu d'insertions ligne par ligne dans la base de données.
- Changement du préfixe des tables en `ansm_`.

### Autres changements
- Documentation du pipeline pour la gestion du rate-limiting de l'EMA.
