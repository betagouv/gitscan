## Changelog : mednum-cli (30 derniers jours, au 23 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des adresses et des lieux de médiation. La mise en cache des adresses a été optimisée et le comportement de l'application a été corrigé pour éviter des erreurs lors de l'absence d'informations d'adresse complètes. Une amélioration a également été apportée pour filtrer les lieux en doublon ayant des identifiants trop volumineux. Enfin, les actions GitHub ont été mises à jour.

### Évolutions fonctionnelles
- Amélioration de la mise en cache des adresses pour une meilleure performance. [#344](https://github.com/anct-cartographie-nationale/mednum-cli/issues/344)
- Correction d'un bug empêchant le bon fonctionnement de l'API BAN lorsque certaines informations d'adresse (commune, code postal, adresse) sont manquantes. [#343](https://github.com/anct-cartographie-nationale/mednum-cli/issues/343)
- Filtrage des lieux de médiation en doublon ayant des identifiants excessivement longs, améliorant ainsi la qualité des données publiées. [#345](https://github.com/anct-cartographie-nationale/mednum-cli/issues/345)

### Évolutions techniques
- Mise à jour des actions GitHub pour optimiser le workflow CI/CD. [#346](https://github.com/anct-cartographie-nationale/mednum-cli/issues/346)
