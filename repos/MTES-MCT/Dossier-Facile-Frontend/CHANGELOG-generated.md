## Changelog : Dossier-Facile-Frontend (30 derniers jours)

### Résumé
Ce changelog couvre une période d'améliorations significatives sur la page de partage de liens, avec une refonte complète de l'interface et de la fonctionnalité. Les utilisateurs peuvent désormais gérer plus facilement leurs liens de partage, les mettre en pause, les modifier et visualiser des informations détaillées. Des corrections d'accessibilité et des améliorations de la robustesse de l'application ont également été apportées.

### Évolutions fonctionnelles
- Refonte complète de la page de partage de liens (partages) avec de nouvelles fonctionnalités : pause/réactivation des liens, suppression, modification, et affichage des détails. (#1867, #1802)
- Ajout d'un bouton pour copier le lien de partage.
- Possibilité de télécharger un PDF des liens de partage.
- Ajout d'une section "Dossier" avec une page de prévisualisation.
- Amélioration de la gestion des erreurs lors du téléchargement de fichiers multiples. (#1869)
- Affichage du nom d'utilisateur au lieu de l'adresse e-mail dans l'interface locataire. (#1202)
- Gestion améliorée de la page de partage lorsque le dossier des colocataires n'est pas entièrement complété. (#1884)
- Correction de l'affichage du message d'annonce dans l'interface locataire. (#1868)
- Ajout d'une fonctionnalité pour mettre en pause les liens de partage de type MAIL.
- Ajout d'une action pour supprimer plusieurs liens de partage en une seule fois.
- Ajout d'une fonctionnalité pour masquer les liens de partage par défaut.
- Ajout d'une page de détails des liens de partage.
- Ajout de la possibilité de modifier les liens de partage.
- Ajout d'une validation de la longueur de l'e-mail.

### Évolutions techniques
- Amélioration de l'accessibilité de l'application, notamment sur la page www et la page de partage. (#1865, #1852)
- Refactoring du code pour améliorer la maintenabilité et la lisibilité.
- Utilisation de composants DSFR pour une meilleure cohérence visuelle.
- Ajout de tests E2E pour la page de partage et correction des tests existants. (#1878, #1887)
- Optimisation des appels API pour améliorer les performances.
- Correction de problèmes de code smells détectés par SonarQube.
- Utilisation de debounce pour améliorer la réactivité de l'input trigram. (#1866)

### Autres changements
- Correction de clés de traduction manquantes. (#1891)
- Mise à jour de la documentation. (#1849)
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour de la version de l'application à 3.4.7.
- Mise à jour de la version de l'application à 3.4.6.
- Mise à jour de la version de l'application à 3.4.5.
- Mise à jour de la version de l'application à 3.4.0.
