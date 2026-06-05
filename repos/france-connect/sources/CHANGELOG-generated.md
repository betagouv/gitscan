## Changelog : sources (30 derniers jours, au 18 mai 2026)

### Résumé
Les dernières mises à jour de FranceConnect se concentrent sur l'amélioration de la sécurité, de l'expérience utilisateur et de la maintenabilité du code. Des corrections ont été apportées pour améliorer la stabilité et la clarté de l'interface utilisateur, notamment au niveau du tableau de bord utilisateur. Des améliorations de journalisation et de traçabilité ont également été implémentées pour faciliter le diagnostic et la résolution des problèmes.

### Évolutions fonctionnelles
- Ajout d'un lien vers un formulaire de support sur les pages d'erreur, incluant des informations contextuelles pertinentes pour une assistance plus rapide. [#issue à retrouver]
- Possibilité de connecter des prestataires de services ayant des exigences de sécurité plus faibles via l'eIDASBridge. [#issue à retrouver]
- Amélioration de l'expérience utilisateur sur le tableau de bord utilisateur, notamment sur mobile, avec une meilleure gestion des entrées utilisateur et une interface plus claire en cas d'expiration de session. [#issue à retrouver]
- Ajout d'un logo pour le futur IdP Yris sur le tableau de bord utilisateur. [#issue à retrouver]
- Ajout d'un message d'avertissement lorsque l'utilisateur désactive tous ses identifiants. [#issue à retrouver]

### Évolutions techniques
- Mise à jour de la dépendance `react-router-dom` vers la version 6.
- Refactorisation de la hiérarchie des dossiers pour améliorer le partage de code entre les applications React.
- Séparation des consommateurs MongoDB par plateforme (FranceConnect niveau d'assurance faible et élevé) pour une meilleure isolation réseau.
- Ajout de logs métier (business logs) au niveau du tableau de bord utilisateur et de FranceConnect+ pour faciliter le suivi et le débogage.
- Ajout de contrôles de cache sur les routes de métadonnées.
- Suppression des claims inutilisés "phone_number" et "address" dans FranceConnect+.
- Ajout de tests BDD pour valider les notifications envoyées lors des changements de préférences d'IdP.
- Ajout de tests BDD et correction d'erreurs sur la page d'historique de connexion de l'utilisateur.
- Ajout de la source IP du client et du port aux logs métier de FranceConnect+.

### Autres changements
- Mise à jour des certificats de l'application local stack.
- Amélioration de la documentation et des fixtures pour l'environnement de développement.
- Déplacement des composants "service providers" vers le répertoire "partners" dans le cadre du développement du tableau de bord partenaire.
- Période de vacances avec peu de changements entre le 10 et le 18 mai 2026.
