## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans le processus de validation du dossier, avec l'ajout de fonctionnalités pour la gestion des garants et l'analyse du logement. Des corrections de bugs ont également été apportées pour améliorer la fiabilité de l'application, notamment concernant l'envoi d'emails et le comportement des boutons dans certaines étapes du processus.

### Évolutions fonctionnelles
- Ajout d'un compteur de caractères pour le message du filigrane (#1977).
- Ajout d'une analyse du logement dans l'étape de résidence (#1971).
- Possibilité de supprimer un garant sur la page de validation du dossier (#1966).
- Amélioration de l'étiquette de l'année de l'avis d'imposition pour la rente viagère et la pension (#1968, #1974).
- Correction d'un bug empêchant l'envoi de l'email du co-locataire à l'API lorsque les noms sont déjà enregistrés (#1934).
- Correction d'un bug où le bouton était incorrectement désactivé dans l'étape de résidence (#1972).
- Suppression du message d'explication concernant le co-locataire lorsque le locataire est de type "JOIN" (#1973, #1975).
- Ajout d'un message d'erreur toast pour le texte personnalisé dépassant la longueur maximale (#1969).

### Évolutions techniques
- Ajout d'un fichier `robots.txt` pour le propriétaire afin d'améliorer le référencement (#1965).
- Amélioration des messages Mattermost et des artefacts vidéo dans les tests E2E (#1970).

### Autres changements
- Suppression de l'enquête pour les codes postaux non vérifiés (#1963).
- Publication de la version 3.5.9 (#1963).
- Correction de la marge supérieure du bouton de suppression du garant (#1967).
- Correction de l'affichage du message de clarification du co-locataire (#1975).
- Suppression des nouvelles lignes dans le texte personnalisé avant la soumission du formulaire (#1976).
