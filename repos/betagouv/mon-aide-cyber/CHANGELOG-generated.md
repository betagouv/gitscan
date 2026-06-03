## Changelog : mon-aide-cyber (30 derniers jours, au 16 mai 2024)

### Résumé
Cette mise à jour apporte des améliorations de sécurité concernant la réception des données via le webhook Livestorm, notamment en validant les données reçues et en limitant la taille du payload. Ces changements visent à renforcer la robustesse du service face à des potentielles attaques.

### Évolutions fonctionnelles
- Sécurité : Ajout d'une validation des données reçues via le webhook Livestorm grâce à un validateur Zod. [#issue à identifier]
- Sécurité : Limitation de la taille du payload reçu via le webhook Livestorm pour prévenir des problèmes de surcharge ou d'attaques. [#issue à identifier]

### Évolutions techniques
- Intégration : Implémentation de la validation Zod pour le webhook Livestorm.
- Sécurité : Mise en place d'une limitation de taille du payload pour le webhook Livestorm.

### Autres changements
- Aucun changement significatif à signaler.
