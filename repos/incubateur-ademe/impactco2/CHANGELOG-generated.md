## Changelog : impactco2 (30 derniers jours)

### Résumé
Ce mois-ci, l'application impactco2 a bénéficié d'améliorations significatives, notamment des corrections de bugs pour une meilleure stabilité, des mises à jour de contenu (FAQ, exemples de détecteur, liens) et des ajustements pour l'intégration via iframes. L'objectif est d'améliorer l'expérience utilisateur et de garantir la fiabilité des informations fournies.

### Évolutions fonctionnelles
- Mise à jour des exemples du détecteur d'impact carbone [#862](https://github.com/incubateur-ademe/impactco2/issues/862).
- Ajout d'une nouvelle FAQ pour répondre aux questions fréquentes des utilisateurs [#859](https://github.com/incubateur-ademe/impactco2/issues/859).
- Mise à jour du lien vers l'étiquette énergétique [#863](https://github.com/incubateur-ademe/impactco2/issues/863).
- Correction d'un bug d'affichage lors de la saisie de nombres [#861](https://github.com/incubateur-ademe/impactco2/issues/861).
- Correction d'une faute de frappe dans la section habillement.
- Amélioration de la suggestion pour la FAQ sur le transport.

### Évolutions techniques
- Correction de problèmes d'initialisation du détecteur, notamment pour éviter les initialisations multiples [#869](https://github.com/incubateur-ademe/impactco2/issues/869).
- Correction d'une erreur d'expression régulière pour la détection de nombres.
- Amélioration de la gestion des tests d'intégration via iframes, notamment en attendant que le réseau soit inactif et en corrigeant des erreurs de configuration (corepack).
- Suppression de la source "negaoctet" en raison de problèmes potentiels [#868](https://github.com/incubateur-ademe/impactco2/issues/868).
- Utilisation de l'attribut `data-name` pour le script dans les iframes [#867](https://github.com/incubateur-ademe/impactco2/issues/867).
- Mise à jour des mappings de statistiques mensuelles et de la configuration de la baseline du navigateur.

### Autres changements
- Correction d'une faute de frappe.
- Correction d'un test iframe défaillant pour la Gaïeté Lyrique.
