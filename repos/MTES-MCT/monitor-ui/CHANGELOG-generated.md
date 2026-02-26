## Changelog : monitor-ui (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations de performance et des corrections de bugs concernant le composant "check tree picker", utilisé pour la sélection multiple d'éléments. Des corrections ont également été apportées pour assurer le bon fonctionnement des calendriers et des champs de date. Enfin, de nouvelles icônes et des couleurs réglementaires ont été ajoutées pour enrichir l'interface utilisateur.

### Évolutions fonctionnelles
- Correction d'un bug dans le composant "check tree picker" concernant le type de données renvoyé lors d'un changement de sélection (#eb6a504).
- Amélioration des performances du composant "check tree picker" grâce à un rendu paresseux des options et à l'ajout d'un debounce pour la recherche (#f00f979, #8f4058d, #1565a1c).
- Ajout d'une référence aux sélecteurs de date pour fermer correctement les calendriers lors d'un clic en dehors (#64740cc).
- Ajout de nouvelles icônes pour les onglets des navires (#19d2fc9).
- Ajout de nouvelles couleurs réglementaires (#c3f5ca4).

### Évolutions techniques
- Refactoring du composant `MultiZoneEditor` en `MultiLocationEditor` avec modification des props (#c41b601).
- Mise à jour de la configuration CI/CD pour l'utilisation du token NPM (#626ac09, #eee2b56, #a5f3b56).
- Ajout de tests unitaires pour le composant "check tree picker" (#ade5b29).

### Autres changements
- Correction d'un bug de comparaison dans le composant "check tree picker" (#8bf8dd9).
