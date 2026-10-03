## Changelog : les-emplois (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois a été marqué par un changement d'identité majeur avec le passage de "Les Emplois de l'inclusion" à "La plateforme de l'inclusion". Les évolutions se sont concentrées sur l'amélioration du parcours d'orientation (notifications automatiques, gestion simplifiée par les services) et sur l'enrichissement de l'expérience utilisateur, notamment via la création d'un nouvel onglet de synthèse pour les profils usagers.

### Évolutions fonctionnelles
- **Identité et Branding** : Rebranding complet du projet (nom, logos, mentions légales et documentation) pour devenir "La plateforme de l'inclusion".
- **Parcours d'orientation** : 
    - Amélioration du suivi avec l'envoi automatique d'e-mails (création, acceptation, refus, expiration et rappels).
    - Possibilité pour les prestataires de services d'accepter ou de décliner une orientation directement depuis l'interface.
    - Ajout de la possibilité pour les usagers de s'inscrire à des événements de mobilisation.
- **Profils Usagers** : 
    - Création d'un nouvel onglet "Synthèse" regroupant les informations clés (conseillers, fin de contrat, dernières candidatures).
    - Mise à jour de la terminologie pour privilégier le terme "Usager" au détriment de "Candidat".
- **Gestion des professionnels et prescripteurs** : 
    - Réorganisation des menus d'affectation (prescripteurs et employeurs).
    - Mise en place d'alertes et de compteurs pour les fins de contrat imminentes.
    - Possibilité pour les professionnels de demander à devenir conseillers.
- **PASS IAE** : Intégration de la clôture des PASS IAE via un formulaire interne (remplaçant l'outil externe Tally) avec notification automatique des usagers.
- **Annuaire Pro** : Ajout de préférences de visibilité et de la géolocalisation des structures dans l'administration.
- **Interface & Accessibilité** : 
    - Ajout d'une déclaration d'accessibilité détaillée.
    - Amélioration de l'ergonomie des filtres de recherche et des notifications à l'écran (toasts).

### Évolutions techniques
- **Traçabilité** : Implémentation d'un système de piste d'audit (audit trail) pour suivre les actions et les sessions utilisateurs.
- **Gestion des utilisateurs et sécurité** : 
    - Refonte des processus de désactivation et de réactivation des comptes.
    - Renforcement de l'obligation d'utiliser ProConnect pour l'authentification des professionnels.
    - Amélioration de la sécurité des appels OIDC (vérification des nonces).
- **Fiches salariés** : Sécurisation du processus d'upload des documents et automatisation du traitement de certaines erreurs de saisie.
- **Performance** : 
    - Optimisation du temps de démarrage du service (gain de 600 ms).
    - Mise en cache des clés d'authentification (JWKS) pour accélérer les connexions.
- **Emails** : Passage au format Markdown pour la rédaction des corps d'e-mails, permettant une mise en forme plus riche.
- **Refactoring** : 
    - Nettoyage important du code avec la suppression de modules obsolètes (DORA, recommandations, GPS).
    - Optimisation de la structure des templates et des requêtes de base de données.

### Autres changements
- **Documentation** : Mise à jour des guides d'installation locale et des explications sur le SSO.
- **Qualité** : Amélioration de la couverture de tests et correction de nombreux problèmes de formatage (espaces, typographie).
