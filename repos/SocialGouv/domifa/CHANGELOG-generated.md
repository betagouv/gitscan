## Changelog : domifa (30 derniers jours, au 5 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment l'intégration de la bibliothèque DSFR, l'ajout d'une page de témoignages et des corrections pour améliorer l'accessibilité et la robustesse de l'application. Des corrections ont également été apportées au backend pour la gestion des SIRET et des référents.

### Évolutions fonctionnelles
- Ajout d'une page de témoignages pour mettre en avant les bénéfices de la plateforme.
- Intégration de la bibliothèque DSFR (Design System for French administration) pour une interface utilisateur plus moderne et conforme aux standards gouvernementaux.
- Ajout d'un détail réseau au backend.
- Amélioration de la gestion des SIRET au backend.

### Évolutions techniques
- Mise à jour et correction de tests unitaires (frontend et backend).
- Amélioration de la sécurité avec l'application de règles de sécurité renforcées.
- Ajout d'un mécanisme de limitation de débit (throttling) pour protéger le backend contre les surcharges.
- Refonte de la gestion des DTO (Data Transfer Object) pour améliorer la robustesse et la sécurité des données.

### Autres changements
- Ajout d'un fichier CLA (Contributor License Agreement) pour les contributions externes.
- Amélioration des logs pour faciliter le débogage et la surveillance de l'application.
- Corrections diverses de l'interface utilisateur (étiquettes de boutons, champs de formulaire, etc.).
- Suppression de l'ancien fichier changelog et remplacement par la gestion automatique via les commits.
- Ajout de `[skip ci]` aux messages de commit de semantic-release pour éviter des boucles d'intégration continue.
