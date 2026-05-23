## Changelog : portail-rse (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la réglementation VSME (Validation des Stratégies de Mesure Environnementale). Plusieurs corrections et optimisations ont été apportées à la qualification des entreprises, notamment concernant la consommation d'énergie, l'affichage des informations et la synchronisation des données avec Metabase. Des améliorations de l'expérience utilisateur et des refactorings techniques ont également été réalisés.

### Évolutions fonctionnelles
- **VSME :** Ajout de la possibilité de choisir le module d'un rapport VSME, synchronisé avec Metabase. [#385951e](https://github.com/betagouv/portail-rse/commit/385951e)
- **VSME :** L'année de clôture est maintenant ajoutée aux rapports VSME. [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b)
- **VSME :** Ajout d'une description pour guider l'utilisateur sur le champ consommation d'énergie. [#97febf0](https://github.com/betagouv/portail-rse/commit/97febf0)
- **VSME :** La consommation d'énergie est désormais un critère nécessaire pour qualifier une entreprise. [#739523d](https://github.com/betagouv/portail-rse/commit/739523d)
- **VSME :** Affichage de la consommation d'énergie dans le formulaire de qualification et dans le résumé de l'entreprise. [#492af87](https://github.com/betagouv/portail-rse/commit/492af87) et [#1a80acd](https://github.com/betagouv/portail-rse/commit/1a80acd)
- **VSME :** Messages d'avertissement améliorés lorsque le profil d'une entreprise est incomplet. [#1a80acd](https://github.com/betagouv/portail-rse/commit/1a80acd)
- **API Sirene :** Gestion du cas où l'API Sirene ne fournit pas le code postal du siège social lors de la création d'une entreprise. [#e6b9159](https://github.com/betagouv/portail-rse/commit/e6b9159)
- **Metabase :** Export de la consommation d'énergie. [#d168e0a](https://github.com/betagouv/portail-rse/commit/d168e0a)

### Évolutions techniques
- **Refactoring VSME :** Simplification des vues de l'espace découverte de la réglementation VSME en réutilisant du code mutualisé. [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d)
- **Refactoring VSME :** Uniformisation du fil d'arianne des différentes parties du tableau de bord. [#4a25145](https://github.com/betagouv/portail-rse/commit/4a25145)
- **Refactoring VSME :** Utilisation de la même logique que les autres réglementations pour les méthodes `criteres_remplis` et `est_soumis`. [#e6fe488](https://github.com/betagouv/portail-rse/commit/e6fe488)
- **Refactoring VSME :** Factorisation de la donnée valide pour éviter la duplication. [#e6a76a4](https://github.com/betagouv/portail-rse/commit/e6a76a4)
- **Refactoring VSME :** Validation d'un champ du formulaire dans la méthode dédiée prévue par Django. [#d50f330](https://github.com/betagouv/portail-rse/commit/d50f330)
- **VSME :** Suppression du code postal du profil affiché sur le tableau de bord. [#d417c25](https://github.com/betagouv/portail-rse/commit/d417c25)
- **VSME :** Suppression du management de l'énergie. [#6e1a505](https://github.com/betagouv/portail-rse/commit/6e1a505)
- **Documentation :** Coloration syntaxique du SQL dans la documentation. [#ed9d129](https://github.com/betagouv/portail-rse/commit/ed9d129)

### Autres changements
- **CSRD :** Indication temporaire concernant la directive Omnibus. [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506)
- **Qualification :** Refus d'une date de clôture dans le futur. [#cd2cb4c](https://github.com/betagouv/portail-rse/commit/cd2cb4c)
- **Audit énergétique :** Prise en compte du nouveau critère de l'audit énergétique. [#a6d3808](https://github.com/betagouv/portail-rse/commit/a6d3808)
- Correction de coquilles sur la VSME. [#628de24](https://github.com/betagouv/portail-rse/commit/628de24)
- Tests complétés sur la simulation VSME. [#16f1383](https://github.com/betagouv/portail-rse/commit/16f1383)
