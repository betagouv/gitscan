## Changelog : otelo (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du tableau de bord avec de nouvelles fonctionnalités de comparaison de scénarios et de prévisualisation des résultats. Des corrections et des améliorations ont également été apportées à la gestion des utilisateurs, des groupes d'EPCI et des scripts CLI.

### Évolutions fonctionnelles
- Ajout de la comparaison en pourcentage entre les leviers et les retours sur investissement (RS) [#40](https://github.com/MTES-MCT/otelo/pull/40).
- Refonte du tableau de bord avec affichage des valeurs dans le tableau comparatif de scénarios [#40](https://github.com/MTES-MCT/otelo/pull/40).
- Prévisualisation des résultats directement dans les formulaires de création/modification [#39](https://github.com/MTES-MCT/otelo/pull/39).
- Possibilité d'usurper l'identité d'un administrateur pour des besoins de test ou de support.
- Ajout d'une nouvelle typologie d'utilisateur et d'une commande CLI associée [#38](https://github.com/MTES-MCT/otelo/pull/38).
- Ajout d'un guide pour l'utilisation des données du parc.
- Amélioration du pilotage de l'application.

### Évolutions techniques
- Correction du script de recalcul du millésime.
- Limitation du nombre de groupes EPCI actifs pour améliorer la performance.
- Correction de la logique de clonage des données en fonction du millésime, avec mise en cache des résultats.
- Suppression de l'envoi d'emails en environnement local pour faciliter le développement.
- Correction de la construction web.
- Vérification de l'appartenance aux groupes EPCI.

### Autres changements
- Amélioration des libellés et des textes de l'interface utilisateur.
- Correction du template Brevo pour la création de mots de passe.
- Correction d'un bug UX.
