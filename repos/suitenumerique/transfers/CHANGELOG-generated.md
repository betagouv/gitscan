## Changelog : transfers (30 derniers jours, au 22/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilité des transferts de fichiers volumineux et le renforcement de la sécurité. Les utilisateurs bénéficient d'une meilleure gestion des téléchargements (reprise possible après interruption) et d'une visibilité accrue sur l'état de réception des fichiers par les destinataires.

### Évolutions fonctionnelles
- **Fiabilité des téléchargements** : amélioration significative de la gestion des téléchargements volumineux et chiffrés. Ils sont désormais plus robustes avec la possibilité de reprendre un téléchargement interrompu, un suivi de la progression et une meilleure gestion des erreurs.
- **Suivi des envois** : affichage de l'état de livraison pour chaque destinataire lors d'un transfert.
- **Expérience de transfert confidentiel** : interface plus lisible et instructions clarifiées pour le partage des clés de chiffrement.
- **Interface utilisateur** : l'application de sélection de services (*app switcher*) peut désormais être repliée pour libérer de l'espace.
- **Widget LaGaufre** : le widget est désormais optionnel et sa configuration est ajustable lors du déploiement.

### Évolutions techniques
- **Sécurité renforcée** : restriction de l'accès à l'administration Django via une liste blanche d'adresses IP et durcissement de la chaîne d'approvisionnement (*supply chain*) du frontend.
- **Sécurisation des téléchargements** : mise en œuvre de capacités signées pour garantir la sécurité lors de la reprise des téléchargements.
- **Optimisation CI/CD** : publication d'une image backend "distroless" pour améliorer la sécurité et réduire la surface d'attaque.
- **Corrections et stabilité** :
    - Résolution de problèmes liés à l'interruption des téléchargements par le *Service Worker*.
    - Optimisation du comportement de l'application lors des rechargements de page (suppression de la pause "préparation").
    - Amélioration de la gestion des scans de fichiers (gestion des budgets d'attente et des doublons).
- **Configuration** : alignement des clés d'environnement CSRF et de l'expéditeur sur les modèles Ansible.
