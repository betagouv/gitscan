## Changelog : mednum-cli (30 derniers jours, au 29 avril 2024)

### Résumé
Cette mise à jour apporte des améliorations à la gestion des adresses et des lieux de médiation, notamment en optimisant l'utilisation de l'API BAN et en filtrant les données dupliquées.  L'URL de l'API Cartographie Nationale a également été mise à jour pour utiliser CloudFront, améliorant potentiellement les performances.

### Évolutions fonctionnelles
- Mise à jour du cache des adresses pour une meilleure performance. [#344](https://github.com/anct-cartographie-nationale/mednum-cli/issues/344)
- Correction : L'appel à l'API BAN est maintenant ignoré lorsque les champs commune, code postal ou adresse sont vides, évitant ainsi des erreurs. [#343](https://github.com/anct-cartographie-nationale/mednum-cli/issues/343)
- Filtrage des lieux de médiation dupliqués avec des identifiants excessivement grands pour améliorer la qualité des données. [#345](https://github.com/anct-cartographie-nationale/mednum-cli/issues/345)

### Évolutions techniques
- Mise à jour de l'URL de l'API Cartographie Nationale pour utiliser CloudFront, optimisant ainsi la distribution du contenu. [#342](https://github.com/anct-cartographie-nationale/mednum-cli/issues/342)
- Mise à jour des actions GitHub pour améliorer le workflow CI/CD. [#346](https://github.com/anct-cartographie-nationale/mednum-cli/issues/346)
