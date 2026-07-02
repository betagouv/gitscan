## Changelog : messages (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec des corrections de bugs et des améliorations de l'interface, notamment dans la composition des messages et la navigation entre les fils de discussion. Des efforts importants ont été faits pour renforcer la sécurité et la robustesse du système, en particulier au niveau de la gestion des emails entrants et sortants. Une refonte technique majeure a également eu lieu, remplaçant Next.js par Vite et TanStack Router pour une meilleure performance et maintenabilité.

### Évolutions fonctionnelles
- Amélioration de l'édition et de la suppression des brouillons de messages.
- Possibilité de créer une boîte de réception sans synchronisation d'identité.
- Amélioration de la navigation et de la sélection dans les fils de discussion, notamment pour l'accessibilité.
- Amélioration du menu déroulant des boîtes de réception.
- Regroupement des paramètres des boîtes de réception dans un dialogue dédié.
- Traduction des espaces réservés des modèles et ajout de la variable `user_name`.
- Ajout d'un indicateur d'état de l'auto-réponse.
- Correction d'un problème d'affichage des sauts de ligne dans le composeur sur Android Chrome.
- Correction d'un problème de sélection des éléments dans les fils de discussion.
- Ajout de l'en-tête `To` aux emails sortants qui en étaient dépourvus.
- Correction de l'ordre et de la sélection par défaut du calendrier lors de la réponse aux invitations.

### Évolutions techniques
- Refonte de l'architecture frontend : remplacement de Next.js par Vite et TanStack Router [#675].
- Migration du parser et du compositeur d'emails vers la nouvelle librairie `jmap-email` [#700].
- Ajout de scripts de publication PyPI pour `jmap-email`.
- Mise à jour de la librairie `dompurify`.
- Mise à jour de la librairie `django-lasuite`.
- Renforcement de la sécurité de la connexion SMTP et de la configuration des proxys.
- Ajout de mesures de défense en profondeur.
- Amélioration de la robustesse de l'analyse des emails entrants.
- Correction d'une course aux permissions de socket Milter au démarrage.

### Autres changements
- Nouvelle illustration pour la page d'accueil [#702].
- Ajout de rapports d'état de l'auto-vérification à Sentry.
- Correction d'un problème d'indentation dans le fichier de configuration Postfix.
- Mise à jour de la version du thème Keycloak.
- Mises à jour de Keycloak (26.6.3 -> 26.6.4).
- Installation de `jmap-email` depuis PyPI.
- Correction d'un langage codé en dur qui pouvait déclencher une traduction automatique.
- Publication de la version 0.8.0 [#715].
