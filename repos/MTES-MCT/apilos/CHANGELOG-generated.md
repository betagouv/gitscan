## Changelog : apilos (30 derniers jours, au 5 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations à la génération de documents, notamment la gestion des images et la normalisation de l'encodage. Des ajustements ont également été effectués sur les templates de documents pour refléter des changements terminologiques et des corrections de données. Enfin, plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction de la normalisation de l'encodage des images lors de la génération de documents, améliorant la qualité et la compatibilité des fichiers produits. [#2164](https://github.com/MTES-MCT/apilos/issues/2164)
- Modification du terme "Prêteur" par "Organisme financeur" dans les templates de documents, pour une terminologie plus précise. [#2171](https://github.com/MTES-MCT/apilos/issues/2171)
- Mise à jour de la mention concernant l'accessibilité dans les documents générés. [#2166](https://github.com/MTES-MCT/apilos/issues/2166)
- Correction du nom du gestionnaire dans le template FicheCAF et suppression du champ `loyer_m2` de la fonction `fiche_caf_doc`. [#2163](https://github.com/MTES-MCT/apilos/issues/2163)
- Ajout d'espaces vides dans le template SEM-template.docx pour une meilleure mise en forme. [#2167](https://github.com/MTES-MCT/apilos/issues/2167)

### Évolutions techniques
- Aucune évolution technique majeure à signaler.

### Autres changements
- Mise à jour de plusieurs dépendances :
    - `@gouvfr/dsfr` (de 1.14.2 à 1.14.4)
    - `@hotwired/turbo` (de 8.0.21 à 8.0.23)
    - `actions/upload-artifact` (de 5 à 7)
    - `beautifulsoup4` (de 4.13.5 à 4.14.3)
    - `orgoro/coverage` (de 3.2 à 3.3)
    - `redis` (de 6.4.0 à 7.4.0)
    - `virtualenv`
