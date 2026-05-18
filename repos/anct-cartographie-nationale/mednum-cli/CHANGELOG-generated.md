## Changelog : mednum-cli (30 derniers jours, au 23 avril 2026)

### Résumé
Cette mise à jour améliore la gestion des adresses et des lieux de médiation numérique. Elle corrige un problème où l'API BAN était appelée inutilement avec des données incomplètes et introduit un filtrage pour éviter les doublons avec des identifiants trop volumineux. Enfin, les actions GitHub ont été mises à jour pour optimiser le processus de CI/CD.

### Évolutions fonctionnelles
- Correction : L'appel à l'API BAN est maintenant ignoré si la commune, le code postal ou l'adresse sont nuls, évitant ainsi des erreurs et optimisant les performances. [#343](https://github.com/anct-cartographie-nationale/mednum-cli/issues/343)
- Amélioration : Les lieux de médiation numérique en doublon avec des identifiants excessivement longs sont maintenant filtrés, améliorant la qualité des données publiées. [#345](https://github.com/anct-cartographie-nationale/mednum-cli/issues/345)
- Amélioration : Mise à jour du cache des adresses pour une meilleure performance et fiabilité. [#344](https://github.com/anct-cartographie-nationale/mednum-cli/issues/344)

### Évolutions techniques
- Mise à jour des actions GitHub pour améliorer le workflow CI/CD. [#346](https://github.com/anct-cartographie-nationale/mednum-cli/issues/346)
