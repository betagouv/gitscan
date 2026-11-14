## Changelog : hubee (30 derniers jours, au 12 novembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'expérience utilisateur sur le portail (meilleure visibilité des agents et des abonnements) et une montée en puissance de l'API. La sécurité et la traçabilité ont également été renforcées, notamment par la correction de plusieurs vulnérabilités et l'amélioration de la gestion des journaux d'audit.

### Évolutions fonctionnelles
- **Interface et navigation du portail** :
    - Amélioration de l'affichage des agents (nom de famille en priorité, date de dernière connexion, détails des champs).
    - Meilleure visibilité des flux (affichage sous forme de tags et utilisation de noms explicites plutôt que des codes).
    - Navigation optimisée vers les télédossiers et affichage détaillé des abonnements.
    - Mise en conformité des pages d'erreur avec les standards DSFR.
- **Gestion des utilisateurs et accès** :
    - Ajout du numéro de téléphone mobile dans les informations de membre.
    - Renforcement de la sécurité des accès : restriction de la lecture des pages d'administration et gestion plus stricte de la casse des codes.
    - Correction de bugs sur la fermeture des télédossiers et le filtrage des flux.
- **Audit et traçabilité** :
    - Ouverture du journal des traces d'audit pour une meilleure visibilité.
    - Conservation des traces de décisions d'accès pendant un an pour répondre aux exigences de conformité.

### Évolutions techniques
- **API** :
    - Mise en place du versionnement de l'API via le chemin d'URL.
    - Standardisation des réponses d'erreur (format JSON avec code et message) et gestion des erreurs 404.
    - Refonte du processus d'invitation des agents : gestion asynchrone (file d'attente), tentatives de renvoi en cas d'échec du serveur d'envoi et meilleur traçage.
    - Amélioration de la robustesse de l'enregistrement des agents et de la validation des données.
- **Sécurité et Infrastructure** :
    - Correction de plusieurs vulnérabilités (CVE) sur les dépendances (Ruby, Rack, Addressable) et les images Docker.
    - Durcissement de la sécurité des conteneurs (utilisation d'images distroless non-root).
    - Migration vers Ruby 4.0.9.
    - Passage de l'envoi des courriels via le service SMTP Brevo.
    - Fiabilisation de la gestion des tâches de fond (Solid Queue).
- **Qualité** :
    - Augmentation de la couverture de tests de bout en bout sur l'API et le portail.

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API concernant l'enregistrement des agents, le processus d'invitation et le versionnement.
- **Configuration** : Amélioration des scripts de préparation (seeds) pour les environnements de test et de développement.
