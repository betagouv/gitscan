## Changelog : les-emplois (30 derniers jours, au 05/08/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec le déploiement du module d'orientation, permettant un suivi plus précis des parcours des candidats. La sécurité a été renforcée par l'introduction de la double authentification (2FA), tandis que l'expérience des professionnels a été simplifiée, notamment pour la gestion des accompagnements et l'automatisation de certaines tâches de maintenance des entreprises.

### Évolutions fonctionnelles
- **Module Orientation** : Ajout d'un menu dédié incluant une vue détaillée et une liste filtrable (par expéditeur, structure, statut ou bénéficiaire). Les statuts d'orientation sont désormais synchronisés automatiquement avec l'outil Dora.
- **Sécurité & Authentification** : Mise en place de la double authentification (2FA/TOTP) avec des guides d'utilisation (QR codes), un menu de configuration et une gestion améliorée des messages d'erreur. Amélioration de la fiabilité des flux de connexion FranceConnect et ProConnect.
- **Gestion des professionnels** : Les professionnels peuvent désormais se désigner eux-mêmes comme le "dernier accompagnateur connu" d'un candidat.
- **Gestion des entreprises** : Désactivation automatique des candidatures spontanées pour les entreprises inactives depuis plus de 90 jours.
- **Parcours candidat** : Amélioration de la saisie des dates de contrat avec l'ajout de composants d'aide contextuelle et de contrôles de validité renforcés.
- **Recherche** : Facilitation de la recherche de candidats par adresse email.
- **Administration** : Nouveau mécanisme de demande de rôle administrateur par email et attribution automatique des administrateurs pour les nouvelles organisations.

### Évolutions techniques
- **Optimisation des performances** : Réduction significative du nombre de requêtes SQL (correction de problèmes de type 1+N) sur les vues de listes de candidats et les recherches d'accompagnateurs.
- **Refactorisation** : Restructuration complète du module `ft_connect` (renommage et réorganisation) et mise en place du "soft-delete" pour les services et les structures.
- **Automatisation** : Création de tâches planifiées pour la synchronisation des données d'orientation et le nettoyage automatique des fichiers inutilisés sur le stockage.
- **Données & Reporting** : Mise à jour du schéma Metabase pour permettre un meilleur suivi des événements de mobilisation et des profils candidats.

### Autres changements
- Mise à jour du thème visuel et des liens d'accessibilité.
- Nettoyage du code et refactorisation de la gestion des permissions et du middleware.
