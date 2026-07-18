## Changelog : histologe (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interconnexion avec les systèmes partenaires (Esabora, SI Santé Habitat), la correction de bugs et l'optimisation de l'interface utilisateur, notamment pour les agents du back-office. Des améliorations de sécurité ont également été apportées.

### Évolutions fonctionnelles

- **Connexion SI :** Optimisation de la page de connexion SI suite aux dernières évolutions et amélioration de la reprise des dossiers en erreur avec Esabora, en ignorant les doublons [#6110].
- **Signalements :**
    - Ajout d'un filtre "Démarche accélérée" dans la liste des signalements [#6041].
    - Possibilité de clôturer temporairement des signalements via une commande dédiée [#6040, #6105].
    - Ajout du suivi automatique interne de l'historique de l'adresse lors de l'enregistrement d'un signalement [#6056].
- **Bailleurs :**
    - Copie de l'interface de login standard pour les bailleurs [#6073].
    - Amélioration de l'interface du formulaire Pro, notamment la navigation au clavier [#6005].
- **Territoire :** Ajout d'une liste des arrêtés dans la gestion du territoire [#6026].
- **Adresses :** Ajout de la zone/coordonnées depuis le profil pro [#6130].
- **SISH :** Envoi de l'adresse complète du bailleur [#6135].
- **Export :** Correction d'un bug empêchant l'export de listes [#6052].
- **Accessibilité :** Amélioration de l'accessibilité du login usager [#6093].

### Évolutions techniques

- **OVH S3 :** Possibilité de désactiver les appels à OVH S3 en cas de dysfonctionnement [#6117].
- **Flush Doctrine :** Rationalisation des flushs Doctrine pour optimiser les performances [#5977].
- **Pagination API :** Correction d'un bug lié à la pagination de l'API [#6075].
- **Sécurité :** Mise à jour de la librairie Jmespath suite à une CVE détectée [#6028].
- **Types :** Modification du label du type d'arrêté [#6097].
- **Carte facile :** Intégration de MapLibre pour la carte facile [#6004].

### Autres changements

- Correction d'une erreur de clé de tableau [#6147, #6148].
- Amélioration de la gestion des erreurs de données et des messages d'erreur pour la connexion SI [#6110].
- Suppression du résumé des suivis généré par l'IA [#6025, #6039].
- Diverses corrections HTML sur la page des dossiers bailleurs [#6076].
- Optimisation du filtre "Dossiers sans activité" dans la liste des signalements [#6125].
- Optimisation de la page de connexion SI [#6138].
- Mise à jour des paquets npm [#6145, #6146, #6036, #6037].
- Mise à jour de composer [#6042, #6043].
- Corrections de typos et améliorations de la documentation.
